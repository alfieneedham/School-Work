from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from math import sin, cos, sqrt
from random import choice, randint

"""
Controls:
    'A' and 'D' are used to move the paddle.
Platforms:
    Blue objects have an elasticity <1, meaning the pinball loses speed. when it collides with them.
    Pink objects have an elasticity of 1, so the pinball neither loses or gains speed.
    The green paddle has an elasticity >1, so the pinball gains speed.
"""

class Pinball(Widget):
    canCollide = True
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def gravity(self):
        terminalVelocity = 15
        accelerationDueToGravity = 0.2
        if self.velocity_y > -terminalVelocity:
            self.velocity_y -= accelerationDueToGravity
        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def detect_collision(self, platform):
        if self.collide_widget(platform):
            return(True)

    def bounce_off_objects(self, platform, position):
        if Pinball.canCollide == True:
            closestCollisionPoint = (None, None)
            # * Each square platform has four collision point, at the centre of its top, bottom, left and right sides.
            # * This code iterates through them, finding the closest of these collision points to the pinball (although this is currently not working).
            for child in platform.children:
                xDistance = child.center_x - position[0]
                yDistance = child.center_y - position[1]
                distanceToPinball = sqrt((xDistance*xDistance) + (yDistance*yDistance))
                #print(child.angle, xDistance, yDistance, child.x, child.y, position[0], position[1], distanceToPinball)
                if closestCollisionPoint[0] == None or distanceToPinball < closestCollisionPoint[0]:
                    closestCollisionPoint = (distanceToPinball, child)
            closestChild = closestCollisionPoint[1]
            # * These are for when the pinball collides with the square. The bumpers have one child, angle of -1.
            if closestChild.angle == 0 or closestChild.angle == 180:
                self.velocity_y *= -platform.elasticity
            if closestChild.angle == 90 or closestChild.angle == 270:
                self.velocity_x *= -platform.elasticity
            # * This is for collision with a bumper. It is treated as a non-glancing collision.
            if closestChild.angle == -1:
                normalVector = Vector(closestChild.center_x - position[0], closestChild.center_y - position[1])
                parallel = normalVector.dot(Vector(self.velocity)) / normalVector.length2() * normalVector
                perpendicular = Vector(self.velocity) - parallel
                self.velocity = perpendicular - parallel
            #print(closestChild.angle)
            # * The pinball is temporarily locked from colliding for a frame. This prevents it from weirdly hovering above the platforms if it comes to rest on them.
            Pinball.canCollide = False
            Clock.schedule_once(Pinball.unlock_collision, 0.001)

    def spawn_pinball(self):
        findXVel = True
        self.center = self.parent.center
        self.y = self.parent.top - 50
        while findXVel == True:
            xVel = randint(-5,6)
            if xVel != 1:
                findXVel = False
        self.velocity = Vector(xVel, 0).rotate(randint(-45,45))

    def bounce_off_walls(self):
        if self.x < self.parent.x or self.right > self.parent.width:
            self.velocity_x *= -1
        if self.top > self.parent.top:
            self.velocity_y *= -1
        if self.y < self.parent.y:
            self.spawn_pinball()
        
    def unlock_collision(dt):
        Pinball.canCollide = True

class RectanglePlatform(Widget):
    toppoint = ObjectProperty(None)
    botpoint = ObjectProperty(None)
    leftpoint = ObjectProperty(None)
    rightpoint = ObjectProperty(None)
class ElasticRectanglePlatform(Widget):
    toppoint = ObjectProperty(None)
    botpoint = ObjectProperty(None)
    leftpoint = ObjectProperty(None)
    rightpoint = ObjectProperty(None)

class Paddle(Widget):
    paddlecomponent = ObjectProperty(None)
    def move_paddle(self, direction):
        if (direction == -1 and self.center_x > self.parent.x) or (direction == 1 and self.center_x < self.parent.width):
            self.x += 10 * direction

class Bumper(Widget):
    bumpercomponent = ObjectProperty(None)
class ElasticBumper(Widget):
    bumpercomponent = ObjectProperty(None)
class TopPoint(Widget):
    pass
class BotPoint(Widget):
    pass     
class LeftPoint(Widget):
    pass
class RightPoint(Widget):
    pass
class BumperComponent(Widget):
    pass
class PaddleComponent(Widget):
    pass

class Scene(Widget):

    def update_scene(self, dt):
        # * When a pinball collides with a platform, its position from the frame of collision is passed into the function to deal with this collision, as this function is called a frame later.
        # * At least that was my reasoning. Looking at this the next day I don't think that's actually the case?
        for platform in self.platforms:
            if self.pinball.detect_collision(platform) == True:
                pinballCoords = (self.pinball.center_x, self.pinball.center_y)
                self.pinball.bounce_off_objects(platform, pinballCoords)
        self.pinball.gravity()
        self.pinball.move()
        self.pinball.bounce_off_walls()
        if self.move_paddle_left == True:
            self.paddle.move_paddle(-1)
        if self.move_paddle_right == True:
            self.paddle.move_paddle(1)

    def keyboard_closed(self):
        print("Keyboard Closed")
        self.keyboard.unbind(on_key_down=self.on_key_down)

    def on_key_down(self, _keyboard, keycode, _text, _modifiers):
        if keycode[1] == "a":
            self.move_paddle_left = True
        if keycode[1] == "d":
            self.move_paddle_right = True
    def on_key_up(self, _keyboard, keycode):
        if keycode[1] == "a":
            self.move_paddle_left = False
        if keycode[1] == "d":
            self.move_paddle_right = False
        
    def initialise_controls(self):
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self.keyboard.bind(on_key_down=self.on_key_down)
        self.keyboard.bind(on_key_up=self.on_key_up)
        self.move_paddle_left = False
        self.move_paddle_right = False

class pinballproject(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        scene = Scene()
        scene.initialise_controls()
        Clock.schedule_interval(scene.update_scene, 1.0 / 60)
        scene.pinball.spawn_pinball()
        return scene
      
if __name__ == "__main__":
    Window.size = (500, 750)
    pinballproject().run()