import curses
import time
import Layout as l


def initialize():
    main_screen = curses.initscr()
    main_screen.clear()
    game_screen = l.Game()
    game_screen.get_screen_borders(main_screen)


initialize()
time.sleep(5)
