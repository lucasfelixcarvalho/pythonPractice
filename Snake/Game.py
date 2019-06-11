import curses
import time
import Layout as l


def initialize():
    screen = curses.initscr()
    screen.clear()
    l.get_screen_borders(screen)
    screen.refresh()


initialize()
time.sleep(5)
