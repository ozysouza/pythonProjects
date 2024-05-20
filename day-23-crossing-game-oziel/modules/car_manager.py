from turtle import Turtle
from modules.level_manager import LevelManager
import random

COLORS = ["red", "blue", "yellow", "orange", "green", "pink"]
STRETCH_WIDTH = 1
STRETCH_LENGTH = 2
X_POSITION = 420
Y_POSITION = range(-200, 201, 20)
START_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.interval = 4
        self.counter = 0
        self.car_speed = START_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        new_car.goto(X_POSITION, random.choice(Y_POSITION))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        # Remove car that have gone off the screen
        self.all_cars = [car for car in self.all_cars if car.xcor() > -X_POSITION]

    def update(self):
        self.counter += 1
        if self.counter % self.interval == 0:
            self.create_car()
        self.move_cars()

    def detect_collision(self, turtle):
        for car in self.all_cars:
            if car.distance(turtle) < 25:
                return True
        return False

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
