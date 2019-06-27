import Engine as E
import curses
import time
import Layout


class EngineConsole(E.Engine):

    def __init__(self):
        super().__init__()

    def run_game(self, screen, window_height, window_width):  # window_height = y axis; window_width = x axis
        self.refresh_snake_screen_position(screen, True)
        food = self.show_food(screen, window_height, window_width)
        direction = 'DOWN'
        dead = False

        while not dead:
            next_key = screen.getch()
            direction_pressed = self.__map_key_direction(next_key)
            new_direction = super().map_direction(direction_pressed, direction)

            direction = new_direction if new_direction is not None else direction
            self.snake.move_snake(direction)

            if super().is_dead(window_height, window_width):
                self.game_over(screen, window_height, window_width)
                dead = True
            else:
                is_food_eaten = super().food_eaten(food)

                if is_food_eaten:
                    super().update_score()
                    food = self.show_food(screen, window_height, window_width)

                self.refresh_snake_screen_position(screen, not is_food_eaten)

    def refresh_snake_screen_position(self, screen, remove_tail):
        for body in self.snake.body:
            screen.addch(body.coord_y, body.coord_x, body.visual_char, curses.A_REVERSE)

        if remove_tail:
            last_tail = self.snake.remove_tail()
            screen.addch(last_tail.coord_y, last_tail.coord_x, ' ')

    def game_over(self, screen, window_height, window_width):
        screen.addstr(int(window_height / 2), int(window_width / 2), 'GAME OVER - score: ' + str(self.score))
        screen.refresh()
        time.sleep(5)
        return True

    def show_food(self, screen, window_height, window_width):
        new_food = super().spawn_food(1, window_height - 2, 1, window_width - 2)
        screen.addch(new_food[0], new_food[1], Layout.Food.FOOD_SYMBOL)
        return new_food

    @staticmethod
    def __map_key_direction(key_pressed):
        if key_pressed == curses.KEY_LEFT:
            return 'LEFT'
        elif key_pressed == curses.KEY_RIGHT:
            return 'RIGHT'
        elif key_pressed == curses.KEY_UP:
            return 'UP'
        elif key_pressed == curses.KEY_DOWN:
            return 'DOWN'
        else:
            return None
