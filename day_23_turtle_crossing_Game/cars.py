from turtle import Turtle
import random

COLORS = ["red","yellow","blue","pink","purple","orange"]
STARTING_MOVE_DISTANCE = 10

class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_number = random.randint(1,5)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=3,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-210,220)
            new_car.penup()
            new_car.goto(400,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_level(self):
        self.car_speed += 5