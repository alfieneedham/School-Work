from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from math import sin, cos
from random import choice, randint

class Marble(Widget):
    canCollide = True
    velocity_x = NumericProperty(1)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def player_input(self):
        pass

    def gravity(self):
        terminalVelocity = 15
        accelerationDueToGravity = 0.5
        if self.velocity_y > -terminalVelocity:
            self.velocity_y -= accelerationDueToGravity
        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def detect_collision(self, platform):
        if self.collide_widget(platform):
            return(True)


 # * this is bad so please find shortest distasnce between chidren and use that one

    def bounce_off_objects(self, platform, elasticity):
        if (self.collide_widget(platform) or platform.parent == Bumper or platform.parent == ElasticBumper) and Marble.canCollide == True:
            if platform.angle == 0 or platform.angle == 180:
                self.velocity_y *= -elasticity
            if platform.angle == 90 or platform.angle == 270:
                self.velocity_x *= -elasticity
            if platform.angle == -1:
                # * This is for collision with a bumper. It is treated as a non-oblique collision.
                normalVector = Vector(platform.center_x - self.center_x, platform.center_y - self.center_y)
                angle = normalVector.angle(Vector(1,0))
                parallel = normalVector.dot(Vector(self.velocity)) / normalVector.length2() * normalVector
                perpendicular = Vector(self.velocity) - parallel
                self.velocity = perpendicular - parallel
            Marble.canCollide = False
            Clock.schedule_once(Marble.unlock_collision, 0.000000000000000000001)

    def spawn_marble(self):
        findXVel = True
        self.center = self.parent.center
        self.y = self.parent.top - 50
        while findXVel == True:
            xVel = randint(-5,5)
            if xVel != 0:
                findXVel = False
        self.velocity = Vector(xVel, 0).rotate(randint(-30, 30))

    def bounce_off_walls(self):
        if self.x < self.parent.x or self.right > self.parent.width:
            self.velocity_x *= -1
        if self.top > self.parent.top:
            self.velocity_y *= -1
        if self.y < self.parent.y:
            self.spawn_marble()
        
    def unlock_collision(dt):
        Marble.canCollide = True

class RectanglePlatform(Widget):
    topline = ObjectProperty(None)
    botline = ObjectProperty(None)
    leftline = ObjectProperty(None)
    rightline = ObjectProperty(None)
class ElasticRectanglePlatform(Widget):
    topline = ObjectProperty(None)
    botline = ObjectProperty(None)
    leftline = ObjectProperty(None)
    rightline = ObjectProperty(None)

class Paddle(Widget):
    paddlecomponent = ObjectProperty(None)
    def move_paddle(self, direction):
        if (direction == -1 and self.center_x > self.parent.x) or (direction == 1 and self.center_x < self.parent.width):
            self.x += 10 * direction

class Bumper(Widget):
    bumpercomponent = ObjectProperty(None)
class ElasticBumper(Widget):
    bumpercomponent = ObjectProperty(None)
class TopLine(Widget):
    pass
class BotLine(Widget):
    pass     
class LeftLine(Widget):
    pass
class RightLine(Widget):
    pass
class BumperComponent(Widget):
    pass
class PaddleComponent(Widget):
    pass

class Scene(Widget):

    def update_scene(self, dt):
        for i in self.platforms:
            if self.marble.detect_collision(i) == True:
                for child in i.children:
                    self.marble.bounce_off_objects(child, i.elasticity)
        self.marble.gravity()
        self.marble.move()
        self.marble.player_input()
        self.marble.bounce_off_walls()
        if self.move_paddle == True:
            self.paddle.move_paddle(self.direction)

    def keyboard_closed(self):
        print("Lost keyboard")
        self.keyboard.unbind(on_key_down=self.on_key_down)

    def on_key_down(self, _keyboard, keycode, _text, _modifiers):

        if keycode[1] == "a":
            self.move_paddle = True
            self.direction = -1
        if keycode[1] == "d":
            self.move_paddle = True
            self.direction = 1

    def on_key_up(self, _keyboard, keycode):
        if keycode[1] == "a" or keycode[1] == "d":
            self.move_paddle = False
        
    def initialise_controls(self):
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self.keyboard.bind(on_key_down=self.on_key_down)
        self.keyboard.bind(on_key_up=self.on_key_up)
        self.move_paddle = False
        self.direction = 0

class awesomeMarbleRunApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        scene = Scene()
        scene.initialise_controls()
        Clock.schedule_interval(scene.update_scene, 1.0 / 60)
        return scene
      
if __name__ == "__main__":
    Window.size = (500, 750)
    awesomeMarbleRunApp().run()