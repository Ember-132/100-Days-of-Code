import time
from turtle import Screen
from cars import CarManager
from user import User
from scoreboard import Writing

screen = Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
screen.bgcolor("black")

timmy = User()
cars = CarManager()
scoreboard = Writing()

screen.listen()
screen.onkey(timmy.up,"w")
screen.onkey(timmy.down,"s")
screen.onkey(timmy.move_right,"d")
screen.onkey(timmy.move_left,"a")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if abs(timmy.xcor() - car.xcor()) < 39 and abs(timmy.ycor() - car.ycor()) < 35:
            game_is_on = False
            scoreboard.game_over()

    if timmy.ycor() == 300:
            scoreboard.update()
            timmy.back_to_base()
            cars.increase_level()


screen.exitonclick()
