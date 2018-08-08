import RPi.GPIO as GPIO
import movements
import time
import curses

robot = movements.robot()

def move(char):
    if char == curses.KEY_UP:
        screen.addstr(0,0, 'up   ')
        robot.forward()

    elif char == curses.KEY_DOWN:
        screen.addstr(0,0,'down ')
        robot.backward()

    elif char == curses.KEY_LEFT:
        screen.addstr(0,0,'left ')
        robot.right()

    elif char == curses.KEY_RIGHT:
        screen.addstr(0,0, 'right')
        robot.left()

    elif char == 32:
        screen.addstr(0,0,'stop ')
        robot.stop()

screen = curses.initscr()

curses.noecho()

curses.cbreak()

screen.keypad(True)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)     # motor 1, forward, top right
GPIO.setup(11, GPIO.OUT)    # motor 1, backward, top right

GPIO.setup(13, GPIO.OUT)    # motor 2, forward, top left
GPIO.setup(15, GPIO.OUT)    # motor 2, backward, top left

GPIO.setup(12, GPIO.OUT)    # motor 3, forward, bottom right
GPIO.setup(16, GPIO.OUT)    # motor 3, backward, bottom right

GPIO.setup(18, GPIO.OUT)    # motor 4, forward, botton left
GPIO.setup(22, GPIO.OUT)    # motor 4, backward, bottom left

GPIO.output(7, False)       # set everything to false at startup
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)
GPIO.output(12, False)
GPIO.output(16, False)
GPIO.output(18, False)
GPIO.output(22, False)

try:
    while True:
        char = screen.getch()

        move(char)

finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
