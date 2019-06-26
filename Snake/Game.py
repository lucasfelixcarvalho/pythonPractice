import curses
from EngineConsole import EngineConsole as Engine


def main(main_screen):
    curses.curs_set(0)
    curses.cbreak()

    main_screen.keypad(True)
    main_screen.clear()
    main_screen.timeout(500)
    main_screen.border(0)

    window_height, window_width = main_screen.getmaxyx()
    e = Engine()
    e.run_game(main_screen, window_height, window_width)


curses.wrapper(main)
