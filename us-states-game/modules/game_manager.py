from turtle import Screen, Turtle
import pandas as pd

STATES_PATH = "/home/oziel/PycharmProjects/us-states-game/resources/50_states.csv"
df = pd.read_csv(STATES_PATH)


class GameManager(Turtle):
    game_screen = Screen()

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.answer = ""
        self.guessed_states = []

    def check_answer(self):
        self.answer = self.game_screen.textinput(
            title="Guess the State",
            prompt="What's the state's name?"
        ).strip().title()

        if self.answer in df.state.values:
            self.state_position()
            self.write(f"{self.answer}")
            self.guessed_states.append(self.answer)
            return True
        else:
            return False

    def add_missing_states(self):
        all_states = df.state.to_list()
        for state in all_states:
            if state not in self.guessed_states:
                st = df[df.state == state]
                self.goto(st.x.iloc[0], st.y.iloc[0])
                self.write(f"{state}")

    def state_position(self):
        state = df[df.state == self.answer]
        x_pos = state.x.iloc[0]
        y_pos = state.y.iloc[0]
        self.goto(x_pos, y_pos)

