from turtle import Turtle

class Writing(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write_instruction(self):
        self.goto(-285,265)
        self.pensize(50)
        self.write("Type 'reset' to reset the game. Type 'exit' or press 'Cancel' to quit the game.",font=("Arial", 12, "bold"))

    def write_state(self,answer,x,y):
        self.goto(x,y)
        self.write(f"{answer}",align="center",font=("Arial", 10, "normal"))

    def clear_screen(self):
        self.clear()