from turtle import Turtle
from modules.scoreboard import Scoreboard


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.scoreboard = Scoreboard()

    def throw(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def detect_collision_on_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def detect_collision_on_paddle(self, r_paddle, l_paddle):
        if self.distance(r_paddle) < 30 and self.xcor() > 320 or self.distance(l_paddle) < 30 and self.xcor() < -320:
            self.bounce_x()

    def reset_position(self):
        self.bounce_x()
        self.goto(0, 0)
        self.move_speed = 0.1

    def detect_miss(self):
        if self.xcor() > 390:
            self.scoreboard.l_point()
            self.reset_position()

        if self.xcor() < -390:
            self.scoreboard.r_point()
            self.reset_position()


