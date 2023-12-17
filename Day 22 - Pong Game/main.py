import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Pong Game")


l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

ball = Ball(0, 0)

screen.listen()
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')

if __name__ == '__main__':
    in_process = True
    while in_process:
        time.sleep(0.1)
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(r_paddle) < 25 and ball.xcor() > 320 or ball.distance(l_paddle) < 25 and ball.xcor() < -320:
            ball.bounce_x()

        if ball.xcor() > 400 or ball.xcor() < -400:
            ball.restart()
        screen.update()

screen.exitonclick()
