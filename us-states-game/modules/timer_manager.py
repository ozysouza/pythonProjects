from turtle import Screen, Turtle
from modules.game_manager import GameManager

STYLE = ("courier", 30, "italic")


class TimerManager(Turtle):
    game_screen = Screen()

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(150, 250)
        self.total_time = 600
        self.time_running = False

    def start_timer(self):
        if not self.time_running:
            self.time_running = True
            self.update_timer()

    def update_timer(self):
        minutes = self.total_time // 60
        seconds = self.total_time % 60
        self.clear()
        self.write(f"{minutes:02}:{seconds:02}", align="center", font=("Arial", 24, "normal"))

        if self.total_time > 0:
            self.total_time -= 1
            self.game_screen.ontimer(self.update_timer, 1000)  # Schedule the function to run again in 1 second
            return True
        else:
            self.end_game()

    def end_game(self):
        self.clear()
        self.goto(0, 320)
        self.write("Time's up! Game Over!", align="center", font=("Arial", 24, "normal"))
        self.total_time = 0

        game_manager = GameManager()
        game_manager.add_missing_states()
