from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class Marble(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def gravity(self):
        terminalVelocity = 10
        accelerationDueToGravity = 0.3
        if abs(self.velocity_y) < terminalVelocity:
            self.velocity_y -= accelerationDueToGravity
        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Platform(Widget):
    def detect_collision(self, marble):
        if self.collide_widget(marble):
            print("Collided!")

class Scene(Widget):
    marble = ObjectProperty(None)
    platform = ObjectProperty(None)

    def update_scene(self, dt):
        self.marble.gravity()
        self.marble.move()
        self.platform.detect_collision(self.marble)

class awesomeMarbleRunApp(App):
    def build(self):
        scene = Scene()
        Clock.schedule_interval(scene.update_scene, 1.0 / 60.0)
        return scene
        
    
if __name__ == "__main__":
    Window.size = (750, 1000)
    awesomeMarbleRunApp().run()
