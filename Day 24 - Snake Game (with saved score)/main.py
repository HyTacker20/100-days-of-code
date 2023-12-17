import time
from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.right, 'd')

if __name__ == '__main__':
    in_process = True
    while in_process:
        screen.update()
        time.sleep(0.1)

        snake.move()

        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) <= 10:
                scoreboard.reset()
                snake.reset()

        if snake.head.distance(food) < 15:
            snake.grow()
            food.refresh()
            scoreboard.add_score()

screen.exitonclick()
