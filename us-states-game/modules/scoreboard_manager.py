from turtle import Turtle

STYLE = ("courier", 15, "italic")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.total_score = 50
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-100, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score {self.score} /{self.total_score}", font=STYLE, )

    def add_point(self):
        self.score += 1
        self.update_score()

