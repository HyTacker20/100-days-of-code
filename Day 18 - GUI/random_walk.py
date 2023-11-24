import random
from turtle import Turtle, Screen

colors = ["red", "green", "orange", "blue", "brown", "violet", "pink"]
my_turtle = Turtle()


def randomize_color():
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    my_turtle.color(R, G, B)


def random_turn_and_move():
    x = random.randrange(0, 361, 90)
    print(x)
    angle = x
    my_turtle.right(angle)
    my_turtle.forward(20)


screen = Screen()
screen.colormode(255)
my_turtle.shape("turtle")
my_turtle.width(10)
while True:
    randomize_color()
    random_turn_and_move()
