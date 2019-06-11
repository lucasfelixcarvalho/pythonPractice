import Snake as s
import curses

snake = s.Snake()


def start_game(screen):
    __update_snake(screen)


def __update_snake(screen):
    for position in snake.snake:
        screen.addstr(position[0], position[1], position[2])

    screen.refresh()
