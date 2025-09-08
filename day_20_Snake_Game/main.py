import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on = True
food_eaten = 0

beating_high_score = True
while beating_high_score:
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()


        #if snake collides with food, increase score and refresh food location
        if food.x_lb(food_eaten) <= snake.head.xcor() <= food.x_hb(food_eaten) and food.y_lb(food_eaten) <= snake.head.ycor() <= food.y_hb(food_eaten):
            food.eat_food(food_eaten)
            food_eaten +=1
            scoreboard.increase_score()
            snake.add_segment()

        #if snake head collides with any segment of the tail
        if snake.has_hit_self():
            # scoreboard.game_over()
            snake.game_reset()
            scoreboard.compare_high_score()


        #if snake collides with wall, end program and print GAME OVER
        if snake.out_of_bounds():
            snake.game_reset()
            # scoreboard.game_over()
            scoreboard.compare_high_score()




screen.exitonclick()
print(f"GAME OVER! You scored {food_eaten} points!")



