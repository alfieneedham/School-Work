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

class Scene(Widget):
    marble = ObjectProperty(None)

    def initialise_scene(self):
        self.marble.center = self.center


class AwesomeMarbleRunApp(App):
    def build(self):
        scene = Scene()
        scene.initialise_scene()
        return scene
    
if __name__ == "__main__":
    AwesomeMarbleRunApp().run()
