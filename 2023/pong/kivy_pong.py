from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint, choice
from math import sqrt
#from win32api import GetKeyState
# pip install pywin32

class PongPaddle(Widget):    
    score = NumericProperty(0)  
     
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            maxSpeed = 100000000000
            offset = (ball.center_y - self.center_y) / (self.height / 2)           
            bounced = Vector(-1 * vx, vy)           
            if sqrt((vx ** 2) + (vy ** 2)) <= maxSpeed:
                vel = bounced * 1.05
            else:
                vel = bounced
            ball.velocity = vel.x, vel.y + (offset * 1.75)
            
#    def move_paddle(self, direction):
#            self.y += (7 * direction)
            
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(0, 0)):
        self.player1.y = self.center_y - 100
        self.player2.y = self.center_y - 100
        self.ball.center = self.center
        xVelocities = [-4, 4]
        if vel != (0, 0):
            self.ball.velocity = Vector(vel[0], vel[1]).rotate(randint(-15, 15))
        else:
            self.ball.velocity = Vector(choice(xVelocities), 0).rotate(randint(-15, 15))

    def update(self, dt):
        
        self.ball.move()
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        # W:
#        if GetKeyState(0x57) < 0:
#            self.player1.move_paddle(1)
        # S:
#        if GetKeyState(0x53) < 0:
#            self.player1.move_paddle(-1)
        # Up:
#        if GetKeyState(0x26) < 0:
#            self.player2.move_paddle(1)
        # Down:
#        if GetKeyState(0x28) < 0:
#            self.player2.move_paddle(-1)
        
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1
        
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
            
    def on_touch_down(self, touch):
        if touch.x <= self.width * 2 / 5:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3 / 5:
            self.player2.center_y = touch.y
                   
    def on_touch_move(self, touch):
        if touch.x <= self.width * 2 / 5:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3 / 5:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        colours = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
        Window.clearcolor = (choice(colours),choice(colours),choice(colours),1)
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == "__main__":
    PongApp().run()