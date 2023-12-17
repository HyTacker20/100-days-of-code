import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars: list[turtle.Turtle] = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = turtle.Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(1, 2)
        car.setheading(180)
        car.up()
        car.goto(300, random.randint(-260, 280))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
