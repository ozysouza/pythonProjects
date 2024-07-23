from modules.screen_manager import ScreenGame
from modules.car_manager import CarManager
from modules.turtle_manager import TurtleManager
from modules.level_manager import LevelManager
import time

screen = ScreenGame()
car_manager = CarManager()
turtle_manager = TurtleManager()
level_manager = LevelManager()

screen.on_listen()
screen.on_key(turtle_manager.move_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update_screen()
    car_manager.update()

    if turtle_manager.ycor() == 300:
        turtle_manager.reset_turtle()
        level_manager.increase_level()
        car_manager.increase_speed()

    if car_manager.detect_collision(turtle_manager):
        level_manager.game_over()
        is_game_on = False


screen.exit()

