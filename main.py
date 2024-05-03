from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

turtle = Turtle()
turtle.shape("square")
turtle.color("white")
turtle.setheading(90)
turtle.shapesize(stretch_len=5, stretch_wid=1)
turtle.penup()
turtle.goto(x=350, y=0)


def move_up():
    turtle.forward(20)


def move_down():
    turtle.backward(20)


screen.listen()
screen.onkeypress(key="Up", fun=move_up)
screen.onkeypress(key="Down", fun=move_down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
