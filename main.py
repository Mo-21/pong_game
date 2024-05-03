from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(x=350, y=0)
paddle_l = Paddle(x=-350, y=0)

ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_r.move_up)
screen.onkeypress(key="Down", fun=paddle_r.move_down)
screen.onkeypress(key="w", fun=paddle_l.move_up)
screen.onkeypress(key="s", fun=paddle_l.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
