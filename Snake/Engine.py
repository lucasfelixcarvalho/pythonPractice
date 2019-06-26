import Snake as S
import random


class Engine:
    def __init__(self):
        self.snake = S.Snake()
        self.score = 0

    def run_game(self, screen, window_height, window_width):
        pass

    def __refresh_snake_screen_position(self, screen, remove_tail):
        pass

    @staticmethod
    def map_direction(new_direction, current_direction):  # base class. Change key_pressed to new_direction string (LEFT, UP...)
        if new_direction == 'LEFT' and current_direction != 'RIGHT':
            return 'LEFT'
        elif new_direction == 'RIGHT' and current_direction != 'LEFT':
            return 'RIGHT'
        elif new_direction == 'DOWN' and current_direction != 'UP':
            return 'DOWN'
        elif new_direction == 'UP' and current_direction != 'DOWN':
            return 'UP'
        else:
            return None

    def spawn_food(self, y_border, x_border):  # base class. Return the X/Y position of the food
        create_food = True
        new_food = (0, 0)

        while create_food:
            new_food = (random.randint(1, y_border - 2), random.randint(1, x_border - 2))

            if not self.snake.is_position_snake(new_food[0], new_food[1]):
                create_food = False

        return new_food

    def food_eaten(self, food):
        if food[0] == self.snake.snake_head.coord_y and food[1] == self.snake.snake_head.coord_x:
            return True
        else:
            return False

    def is_dead(self, window_height, window_width):
        if self.snake.snake_head.coord_x == (window_width - 1) \
                or self.snake.snake_head.coord_y == (window_height - 1) \
                or self.snake.snake_head.coord_x == 0 \
                or self.snake.snake_head.coord_y == 0:
            return True
        if self.snake.collide_itself():
            return True

        return False

    def __game_over(self, screen, window_height, window_width):
        pass

    def update_score(self):  # base class.
        self.score += 1
