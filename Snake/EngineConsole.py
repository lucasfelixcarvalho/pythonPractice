import Engine as E
import curses
import time
import Layout


class EngineConsole(E.Engine):

    def __init__(self):
        super().__init__()

    def refresh_snake_screen_position(self, screen, remove_tail):
        for body in self.snake.body:
            screen.addch(body.coord_y, body.coord_x, body.visual_char, curses.A_REVERSE)

        if remove_tail:
            last_tail = self.snake.remove_tail()
            screen.addch(last_tail.coord_y, last_tail.coord_x, ' ')

    @staticmethod
    def game_over(screen, window_height, window_width, score):
        screen.addstr(int(window_height / 2), int(window_width / 2), 'GAME OVER - score: ' + str(score))
        screen.refresh()
        time.sleep(5)
        screen.endwin()

    @staticmethod
    def show_food(screen, window_height, window_width):
        new_food = super().spawn_food(window_height, window_width)
        screen.addch(new_food[0], new_food[1], Layout.Food.FOOD_SYMBOL)
