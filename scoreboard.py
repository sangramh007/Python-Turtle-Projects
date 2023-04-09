from turtle import Turtle

FONT = ("Verdana", 15, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.show_score()

    def update_score(self):
        self.score += 1
        self.show_score()
