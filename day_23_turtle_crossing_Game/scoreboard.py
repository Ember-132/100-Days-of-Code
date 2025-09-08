from turtle import Turtle

level_font = ("Arial", 20, "normal")
end_message_font = ("Arial", 40, "normal")

class Writing(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.show_level()

    def show_level(self):
        self.goto(0,260)
        self.pendown()
        self.write(f"Level: {self.level}",align="center",font = level_font)

    def update(self):
        self.level += 1
        self.clear()
        self.goto(0, 260)
        self.pendown()
        self.write(f"Level: {self.level}", align="center", font=level_font)

    def game_over(self):
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", align="center", font=end_message_font)

    def winner(self):
        self.goto(0, 0)
        self.pendown()
        self.write(f"YOU WIN", align="center", font=end_message_font)
