import Snake as S
import random


class Engine:
    def __init__(self):
        self.snake = S.Snake()

    def run_game(self, screen, window_height, window_width):  # window_height = y axis; window_width = x axis
        self.__start_game(screen)
        score = 0

        food_location = self.spawn_food(window_height, window_width)
        direction = 'DOWN'
        while True:  # how the loop will be handled?
            next_key = screen.getch()  # how I'll receive the key pressed ??
            new_direction = self.map_direction(next_key, direction)

            direction = new_direction if new_direction is not None else direction

            self.snake.move_snake(direction)  # return the snake to the caller

            if self.__is_dead(window_height, window_width, self.snake.body[0]):
                self.__game_over(screen, window_height, window_width, score)

            is_food_eaten = self.__food_eaten(food_location, self.snake.body[0])

            if is_food_eaten:
                score = self.__update_score(score)
                food_location = self.spawn_food(window_height, window_width)

            self.__refresh_snake_screen_position(screen, not is_food_eaten)

    def __start_game(self, screen):
        self.__refresh_snake_screen_position(screen, True)

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

    @staticmethod
    def __food_eaten(food, snake_head):  # base class.
        if food[0] == snake_head.coord_y and food[1] == snake_head.coord_x:
            return True
        else:
            return False

    def __is_dead(self, window_height, window_width, snake_head):  # base class.
        if snake_head.coord_x == (window_width - 1) or snake_head.coord_y == (window_height - 1) or snake_head.coord_x == 0 or snake_head.coord_y == 0:
            return True
        if self.snake.collide_itself():
            return True

        return False

    def __game_over(self, screen, window_height, window_width, score):
        pass

    @staticmethod
    def __update_score(score):  # base class.
        return score + 1
