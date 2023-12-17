import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.finish_line_y = FINISH_LINE_Y
        self.shape("turtle")
        self.setheading(90)
        self.up()
        self.goto(STARTING_POSITION)

    def move(self):
        x_pos, y_pos = self.xcor(), self.ycor()
        self.goto(x_pos, y_pos+MOVE_DISTANCE)

    def refresh_position(self):
        self.goto(STARTING_POSITION)

