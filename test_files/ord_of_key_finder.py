import curses

screen = curses.initscr()

curses.noecho()

curses.cbreak()

screen.keypad(True)

try:
    while True:
        char = screen.getch()

        screen.addstr(0,0, str(char) + '    ')

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
