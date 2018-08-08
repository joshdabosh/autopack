import RPi.GPIO as GPIO
import curses
import time

screen = curses.initscr()

curses.noecho()

curses.cbreak()

screen.keypad(True)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)     # motor 1, forward, top right
GPIO.setup(11, GPIO.OUT)    # motor 1, backward, top right

GPIO.setup(13, GPIO.OUT)    # motor 2, forward, top left
GPIO.setup(15, GPIO.OUT)    # motor 2, backward, top left

GPIO.output(7, False)       # set everything to false at startup
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)

try:
    while True:
        char = screen.getch()
        screen.addstr(0,0,str(char))

        if char == '':
            screen.addstr(0,0,'nuttin')
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)

        if char == curses.KEY_UP:
            screen.addstr(0,0, 'up   ')
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(7, True)
            GPIO.output(13, True)

        elif char == curses.KEY_DOWN:
            screen.addstr(0,0,'down ')
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(11, True)
            GPIO.output(15, True)

        elif char == curses.KEY_LEFT:
            screen.addstr(0,0,'left ')
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(11, True)
            GPIO.output(13, True)

        elif char == curses.KEY_RIGHT:
            screen.addstr(0,0, 'right')
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(7, True)
            GPIO.output(15, True)

        elif char == 32:
            screen.addstr(0,0,'stop ')
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)

        else:
            screen.addstr(0,0,'nuttin')
            GPIO.output(7, False)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
