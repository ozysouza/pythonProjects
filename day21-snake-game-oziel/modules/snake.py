from turtle import Turtle, Screen

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for s_index in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[s_index - 1].xcor()
            new_y = self.snakes[s_index - 1].ycor()
            self.snakes[s_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def collision_on_x(self):
        return self.head.xcor() > 290 or self.head.xcor() < -290

    def collision_on_y(self):
        return self.head.ycor() > 290 or self.head.ycor() < -290

    def collision_on_body(self):
        for snake in self.snakes[1:]:
            if self.head.distance(snake) < 10:
                return True

    def reset_snake(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
