import random
from turtle import Turtle, Screen

colors = ["red", "green", "orange", "blue", "brown", "violet", "pink"]
my_turtle = Turtle()


def randomize_color():
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    my_turtle.color(R, G, B)


screen = Screen()
screen.colormode(255)
my_turtle.speed(0)

square_size = 600
dots_in_row = 2

x_y = square_size / 2
my_turtle.up()
start = (my_turtle.pos()[0] - x_y, my_turtle.pos()[1] - x_y)
my_turtle.setpos(start)

row = 0
while row != dots_in_row:
    my_turtle.down()
    randomize_color()
    my_turtle.dot(int(square_size / dots_in_row / 3))
    my_turtle.up()
    my_turtle.forward(square_size / dots_in_row)
    if my_turtle.xcor() == x_y:
        my_turtle.up()
        my_turtle.setpos(-x_y, my_turtle.ycor() + square_size / dots_in_row)
        row += 1

screen.exitonclick()
