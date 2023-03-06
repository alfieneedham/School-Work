from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class Marble(Widget):
    canCollide = True

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def gravity(self):
        terminalVelocity = 15
        accelerationDueToGravity = 0.5
        if self.velocity_y > -terminalVelocity:
            self.velocity_y -= accelerationDueToGravity
        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        
    def unlock_collision(delta):
        Marble.canCollide = True
        print("Unlocked")

class HorizontalLine(Widget):
    def detect_collision(self, marble):
        coefficientOfRestitution = 0.8
        if self.collide_widget(marble) and Marble.canCollide == True:
            print("Collided!")
            marble.velocity_y *= -coefficientOfRestitution
            Marble.canCollide = False
            Clock.schedule_once(Marble.unlock_collision, 0.00001)
            print(self.angle)
            return(True)
        else:
            return(False)
        
class VerticalLine(Widget):
    def detect_collision(self, marble):
        coefficientOfRestitution = 0.8
        if self.collide_widget(marble) and Marble.canCollide == True:
            print("Collided!")
            marble.velocity_y *= -coefficientOfRestitution
            Marble.canCollide = False
            Clock.schedule_once(Marble.unlock_collision, 0.00001)
            print(self.angle)
            return(True)
        else:
            return(False)

class Scene(Widget):
    marble = ObjectProperty(None)
    platform = ObjectProperty(None)
    verticalline = ObjectProperty(None)
    # * i think this is the issue but idk

    def update_scene(self, dt):
        # * This prevents gravity from activating the same frame as velocity is changed due to collision, which causes some interesting bugs.
        if self.platform.detect_collision(self.marble) == False:
            self.marble.gravity()
        self.marble.move()

class awesomeMarbleRunApp(App):
    def build(self):
        scene = Scene()
        Clock.schedule_interval(scene.update_scene, 1.0 / 120.0)
        return scene
        
    
if __name__ == "__main__":
    Window.size = (750, 750)
    awesomeMarbleRunApp().run()
