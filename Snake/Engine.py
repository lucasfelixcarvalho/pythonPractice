import Snake as S
import curses
import random
import Layout
import time

snake = S.Snake()


def run_game(screen, window_height, window_width):  # window_height = y axis; window_width = x axis
    __start_game(screen)
    food_location = __spawn_food(screen, window_height, window_width)
    direction = 'DOWN'
    while True:
        next_key = screen.getch()
        new_direction = __map_direction(next_key)

        direction = new_direction if new_direction is not None else direction

        snake.move_snake(direction)

        if snake.body[0].coord_x == (window_width - 1) or snake.body[0].coord_y == (window_height - 1) or snake.body[0].coord_x == 0 or snake.body[0].coord_y == 0:
            screen.addstr(int(window_height / 2), int(window_width / 2), 'GAME OVER')
            screen.refresh()
            time.sleep(5)
            screen.endwin()

        is_food_eaten = __food_eaten(food_location, snake.body[0])

        if is_food_eaten:
            food_location = __spawn_food(screen, window_height, window_width)

        __refresh_snake_screen_position(screen, not is_food_eaten)


def __start_game(screen):
    __refresh_snake_screen_position(screen, True)


def __refresh_snake_screen_position(screen, remove_tail):
    for body in snake.body:
        screen.addch(body.coord_y, body.coord_x, body.visual_char, curses.A_REVERSE)

    if remove_tail:
        last_tail = snake.remove_tail()
        screen.addch(last_tail.coord_y, last_tail.coord_x, ' ')


def __map_direction(key_pressed):
    if key_pressed == curses.KEY_LEFT:
        return 'LEFT'
    elif key_pressed == curses.KEY_RIGHT:
        return 'RIGHT'
    elif key_pressed == curses.KEY_DOWN:
        return 'DOWN'
    elif key_pressed == curses.KEY_UP:
        return 'UP'
    else:
        return None


def __spawn_food(screen, y_border, x_border):
    create_food = True
    new_food = (0, 0)

    while create_food:
        new_food = (random.randint(1, y_border - 2), random.randint(1, x_border - 2))

        if not snake.is_position_snake(new_food[1], new_food[0]):
            create_food = False

    screen.addch(new_food[0], new_food[1], Layout.Food.FOOD_SYMBOL)
    return new_food


def __food_eaten(food, snake_head):
    if food[0] == snake_head.coord_y and food[1] == snake_head.coord_x:
        return True
    else:
        return False
