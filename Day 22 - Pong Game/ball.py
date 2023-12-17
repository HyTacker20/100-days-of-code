from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x, y)

        self.x_move = 10
        self.y_move = 10

    def move(self):
        x, y = self.pos()
        self.goto(x + self.x_move, y + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0, 0)
