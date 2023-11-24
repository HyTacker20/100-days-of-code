import random
from turtle import Turtle, Screen

colors = ["red", "green", "orange", "blue", "brown", "violet", "pink"]

my_turtle = Turtle()
screen = Screen()
my_turtle.shape("turtle")
for corner in range(3, 9):
    my_turtle.color(random.choice(colors))
    for _ in range(corner):
        my_turtle.forward(100)
        my_turtle.right(360 / corner)
screen.exitonclick()
