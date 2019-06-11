import curses
import time
import Layout as l
import Engine as e


def initialize():
    main_screen = curses.initscr()
    main_screen.keypad(True)
    main_screen.clear()

    curses.curs_set(False)

    game_screen = l.Game()
    game_screen.get_screen_borders(main_screen)

    e.run_game(main_screen)


initialize()
time.sleep(5)
