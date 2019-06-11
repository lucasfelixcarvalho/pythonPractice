import curses


def get_screen_borders(screen):
    try:
        for n in range(0, 41):
            screen.addstr(0, n, '_')
            screen.addstr(20, n, '_')

        for n in range(1, 21):
            screen.addstr(n, 0, '|')
            screen.addstr(n, 40, '|')
    except:
        screen.addstr(0, 0, "Windows size not supported")
