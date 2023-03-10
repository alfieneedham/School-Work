from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from math import sin, cos

class Marble(Widget):
    canCollide = True

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def gravity(self):
        terminalVelocity = 15
        accelerationDueToGravity = 0.5 / 4
        if self.velocity_y > -terminalVelocity:
            self.velocity_y -= accelerationDueToGravity
        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def detect_collision(self, platform):
        elasticity = 0.8
        if self.collide_widget(platform) and Marble.canCollide == True:
            print("Collided!", platform.angle)
            if platform.angle == 0 or platform.angle == 180:
                self.velocity_y *= -elasticity
            if platform.angle == 90 or platform.angle == 270:
                self.velocity_x *= -elasticity
            if platform.angle == 45 or platform.angle == 225:
                tempVelocity = self.velocity_y
                self.velocity_y = -elasticity * self.velocity_x
                self.velocity_x = -elasticity * tempVelocity
            if platform.angle == 135 or platform.angle



            # * equation time l;ets govequaitons go ehe por fasvpfr



            Marble.canCollide = False
            Clock.schedule_once(Marble.unlock_collision, 0.01)
            return(True)
        else:
            return(False)
        
    def unlock_collision(dt):
        Marble.canCollide = True
        print("Unlocked")

class RectanglePlatform(Widget):
    topline = ObjectProperty(None)
    botline = ObjectProperty(None)
    leftline = ObjectProperty(None)
    rightline = ObjectProperty(None)
class TopLine(Widget):
    pass
class BotLine(Widget):
    pass     
class LeftLine(Widget):
    pass
class RightLine(Widget):
    pass

class Scene(Widget):
    marble = ObjectProperty(None)
    platform = ObjectProperty(None)

    def update_scene(self, dt):
        for child in self.platform.children:
            if self.marble.detect_collision(child) == False:
                self.marble.gravity()
        self.marble.move()

class awesomeMarbleRunApp(App):
    def build(self):
        scene = Scene()
        Clock.schedule_interval(scene.update_scene, 1.0 / 120.0)
        return scene
        
if __name__ == "__main__":
    Window.size = (500, 750)
    awesomeMarbleRunApp().run()
