import Snake as S
import curses
import random

snake = S.Snake()


def run_game(screen, x_border, y_border):
    __start_game(screen)
    direction = 'DOWN'

    while True:
        __spawn_food(screen, x_border, y_border)
        next_key = screen.getch()
        new_direction = __map_direction(next_key)

        direction = new_direction if new_direction is not None else direction

        snake.move_snake(direction)
        __refresh_snake_screen_position(screen)


def __start_game(screen):
    __refresh_snake_screen_position(screen)


def __refresh_snake_screen_position(screen):
    for body in snake.snake:
        screen.addch(body.column_position, body.row_position, body.visual_char, curses.A_REVERSE)

    last_tail = snake.set_new_tail()
    screen.addch(last_tail.column_position, last_tail.row_position, ' ')


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


def __spawn_food(screen, x_border, y_border):
    create_food = True
    while create_food:
        new_food = (random.randint(1, y_border - 1), random.randint(1, x_border - 1))
        char_at_screen = screen.instr(new_food[0], new_food[1], 1)

        if char_at_screen == '':
            create_food = False

    screen.addch(new_food[0], new_food[1], '#')

