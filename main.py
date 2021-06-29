from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import (
	NumericProperty, ReferenceListProperty, ObjectProperty
	)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
    	if self.collied_widget(ball):
    		vx, vy = ball.velocity
    		offset = (ball.center_y - self.center_y) / (self.height / 2)
    		bounced = Vector(-1 * vx, vy)
    		vel = bounced * 1.1

    		ball.velocity = vel.x, vel.y + offset


class PongBall(Widget)

      # Speed
      velocity_x = NumericProperty(0)
      velocity_y = NumericProperty(0)


      # Vector
      velocity = ReferenceListProperty(velocity_x, velocity_y)

      # Move, move, move!
      def move(self):
      	  self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget)
   ball = ObjectProperty(None) # The connection of the object with the ball
   player1 = ObjectProperty(None)
   player2 = ObjectProperty(None)


def serve_ball(self)
    self.ball.center = self.center
    self.ball.velocity = Vector(4, 0). rotate(randint(0, 360))


    self.player1.bounce_ball(self.ball)
    self.player2.bounce_ball(self.ball)

   def update(self, dt):
   	   self.ball.move() 

       if(self.ball.y < 0) or (self.ball.top > self.height):
       	   self.ball.velocity_y *= -1

       if(self.ball.x < 0) or (self.ball.right > self.width)
           self.ball.velocity_x


class PongApp(App)
   def build(self)
       game = PongGame()
       game.serve_ball()
       Clock.schedule_interval(game.update, 1.0/60)
       return game 

if __name__ == '__main__':
	PongApp().run()
