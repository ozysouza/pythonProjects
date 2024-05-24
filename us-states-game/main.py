from modules.screen_manager import ScreenManager
from modules.game_manager import GameManager
from modules.scoreboard_manager import ScoreBoard
from modules.timer_manager import TimerManager

screen = ScreenManager()
game = GameManager()
score = ScoreBoard()
timer = TimerManager()

timer.start_timer()
while timer.total_time > 0 or game.guessed_states < 50:
    if game.answer == "Exit":
        timer.end_game()
        break

    if game.check_answer():
        score.add_point()

screen.exit()
