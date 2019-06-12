import Snake as S
import curses

snake = S.Snake()


def run_game(screen, x_border, y_border):
    __start_game(screen)

    next_key = screen.getch()

    while next_key == -1:
        next_key = screen.getch()
        snake.move_snake('DOWN')
        __refresh_snake_screen_position(screen)


def __start_game(screen):
    __refresh_snake_screen_position(screen)


def __refresh_snake_screen_position(screen):
    for body in snake.snake:
        screen.addch(body.column_position, body.row_position, body.visual_char, curses.A_REVERSE)

    last_tail = snake.set_new_tail()
    screen.addch(last_tail.column_position, last_tail.row_position, ' ')
