import Snake as S
import curses

snake = S.Snake()


def start_game(screen):
    __update_snake(screen)


def __update_snake(screen):
    for body in snake.snake:
        screen.addstr(body.column_position, body.row_position, body.visual_char, curses.A_REVERSE)

    screen.refresh()
