from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x, y)

    def up(self):
        xcor, ycor = self.pos()
        self.goto(xcor, ycor + 20)

    def down(self):
        xcor, ycor = self.pos()
        self.goto(xcor, ycor - 20)
