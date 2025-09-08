import random
from turtle import Turtle
from snake import OUTER_BOUNDS

NUMBER_OF_FOOD_SEGMENTS = 100
COLORS = ["red","pink", "yellow","blue","purple","green","orange"]

class Food:

    def __init__(self):
        self.food_segments = []
        self.create_food()

    def create_food(self):
        for seg in range(NUMBER_OF_FOOD_SEGMENTS):
            random_x = random.randint(-OUTER_BOUNDS+3, OUTER_BOUNDS-3)
            random_y = random.randint(-OUTER_BOUNDS+3, OUTER_BOUNDS-3)
            random_color = random.choice(COLORS)
            food = Turtle("square")
            food.penup()
            food.turtlesize(1)
            food.color(random_color)
            food.goto(random_x, random_y)
            self.food_segments.append(food)
            if food != self.food_segments[0]:
                food.hideturtle()

    def x_lb(self,food_seg):
        x_lower_boundary = self.food_segments[food_seg].xcor() -25
        return x_lower_boundary

    def x_hb(self,food_seg):
        x_higher_boundary = self.food_segments[food_seg].xcor() + 25
        return x_higher_boundary

    def y_lb(self, food_seg):
        y_lower_boundary = self.food_segments[food_seg].ycor() - 25
        return y_lower_boundary

    def y_hb(self, food_seg):
        y_higher_boundary = self.food_segments[food_seg].ycor() + 25
        return y_higher_boundary

    def eat_food(self,food_seg):
        self.food_segments[food_seg].hideturtle()
        self.food_segments[food_seg+1].showturtle()

