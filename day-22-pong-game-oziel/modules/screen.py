from turtle import Screen


class GameScreen:
    screen = Screen()

    def __init__(self):
        super().__init__()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game!")
        self.screen.tracer(0)

    def update_screen(self):
        self.screen.update()

    def exit(self):
        self.screen.exitonclick()

    def on_listen(self):
        self.screen.listen()

    def on_key(self, func, key):
        self.screen.onkey(func, key)

