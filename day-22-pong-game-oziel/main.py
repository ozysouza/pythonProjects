from modules.screen import GameScreen
from modules.paddles import GamePaddles
from modules.ball import Ball
import time

game_screen = GameScreen()
left_paddle = GamePaddles((-380, 0))
right_paddle = GamePaddles((380, 0))
ball = Ball()


game_screen.on_listen()
game_screen.on_key(left_paddle.go_up, "w")
game_screen.on_key(right_paddle.go_up, "Up")
game_screen.on_key(left_paddle.go_down, "s")
game_screen.on_key(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    game_screen.update_screen()
    ball.throw()
    ball.detect_collision_on_wall()
    ball.detect_collision_on_paddle(right_paddle, left_paddle)
    ball.detect_miss()

game_screen.exit()
