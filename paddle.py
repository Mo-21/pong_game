from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(x=self.x, y=self.y)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
