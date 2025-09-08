import fileinput
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 250)
        self.clear()
        with open("high_score_record.txt", mode ="r") as file:
            self.high_score = int(file.read())
            file.close()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write("GAME OVER",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.goto(0, 250)
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def compare_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("high_score_record.txt", mode ="w") as file:
            file.write(f"{self.high_score}")
            file.close()
        self.update_scoreboard()