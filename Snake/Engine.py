import Snake as S
import curses

snake = S.Snake()


def run_game(screen):
    __start_game(screen)


def __start_game(screen):
    __refresh_snake_screen_position(screen)


def __refresh_snake_screen_position(screen):
    screen.clear()

    for body in snake.snake:
        screen.addstr(body.column_position, body.row_position, body.visual_char, curses.A_REVERSE)

    screen.refresh()
