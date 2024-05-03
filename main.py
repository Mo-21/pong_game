from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle(x=350, y=0)
paddle_l = Paddle(x=-350, y=0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_r.move_up)
screen.onkeypress(key="Down", fun=paddle_r.move_down)
screen.onkeypress(key="w", fun=paddle_l.move_up)
screen.onkeypress(key="s", fun=paddle_l.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
