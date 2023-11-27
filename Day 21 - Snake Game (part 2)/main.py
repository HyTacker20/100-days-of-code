import time
from turtle import Screen

from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()

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

        if snake.head.distance(food) < 15:
            food.refresh()
