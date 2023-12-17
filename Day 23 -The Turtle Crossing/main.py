import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if random.randint(1, 20) in [1, 2, 3, 4]:
        car_manager.generate_car()

    for car in car_manager.cars:
        if car.distance(player) <= 20:
            print(1)
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= player.finish_line_y:
        player.refresh_position()
        car_manager.increase_speed()
        scoreboard.add_level()

    car_manager.move_cars()

    screen.update()

screen.exitonclick()