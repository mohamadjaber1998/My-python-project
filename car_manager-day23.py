from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_car()
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_car(self):
        random_chance = random.randint(0, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(310, random.randint(-250, 250))
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            new_x = car.xcor() - self.STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())

    def increase_level(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
