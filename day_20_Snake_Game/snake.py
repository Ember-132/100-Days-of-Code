from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
OUTER_BOUNDS = 281


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        starting_x_coord = 0
        for seg in range(3):
            snake = Turtle()
            snake.shape("square")
            snake.turtlesize(1)
            snake.penup()
            snake.color("white")
            snake.goto(starting_x_coord, 0)
            starting_x_coord -= 20
            self.snake_segments.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def pause(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def out_of_bounds(self):
        x_co = self.head.xcor()
        y_co = self.head.ycor()
        if x_co >= OUTER_BOUNDS or x_co <= -OUTER_BOUNDS or y_co >= OUTER_BOUNDS or y_co <= -OUTER_BOUNDS:
            return True


    def add_segment(self):
        last_seg_cor = self.snake_segments[-1].position()
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.turtlesize(1)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(last_seg_cor)
        self.snake_segments.append(new_segment)


    def has_hit_self(self):
        for seg in self.snake_segments[1:]:
            if self.head.distance(seg) < 10:
                return True

    def game_reset(self):
        for seg in self.snake_segments:
            seg.goto(0,0)
        for seg in self.snake_segments[3:]:
            seg.hideturtle()
            self.snake_segments.remove(seg)



