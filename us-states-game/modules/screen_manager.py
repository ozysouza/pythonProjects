from turtle import Screen, Turtle
import time

IMAGE_PATH = "../us-states-game/images/blank_states_img.gif"


class ScreenManager(Turtle):
    game_screen = Screen()

    def __init__(self):
        super().__init__()
        self.penup()
        self.game_screen.setup(width=800, height=800)
        self.game_screen.title("U.S States Game")
        self.game_screen.addshape(IMAGE_PATH)
        self.shape(IMAGE_PATH)

    def exit(self):
        self.game_screen.exitonclick()

    def main_loop(self):
        self.main_loop()


