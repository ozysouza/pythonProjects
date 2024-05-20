from turtle import Turtle

TOP_EDGE = 300
START_POSITION = (0, -260)
MOVE_DISTANCE = 20


class TurtleManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.left(90)
        self.goto(START_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(START_POSITION)



