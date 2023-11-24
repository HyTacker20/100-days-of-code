from turtle import Turtle, Screen

my_turtle = Turtle()

screen = Screen()
for _ in range(10):
    my_turtle.forward(10)
    my_turtle.up()
    my_turtle.forward(10)
    my_turtle.down()
screen.exitonclick()
