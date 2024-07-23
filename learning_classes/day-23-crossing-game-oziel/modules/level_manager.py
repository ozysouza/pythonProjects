from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class LevelManager(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-300, 260)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game is Over!", align=ALIGNMENT, font=('Courier', 50, 'normal'))
