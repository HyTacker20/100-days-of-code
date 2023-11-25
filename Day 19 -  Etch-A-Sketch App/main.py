from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()


def move_forwards():
    leo.forward(10)


def move_backwards():
    leo.forward(-10)


def turn_right():
    leo.right(10)


def turn_left():
    leo.left(10)


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)

screen.exitonclick()
