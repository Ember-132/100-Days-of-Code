from turtle import Turtle

class User(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(0,-260)
        self.setheading(90)
        self.shapesize(stretch_len=2,stretch_wid=2)


    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def back_to_base(self):
        self.goto(0,-260)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x =  self.xcor() - 20
        self.goto(new_x, self.ycor())