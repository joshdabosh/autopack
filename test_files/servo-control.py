import RPi.GPIO as GPIO
import time
from Tkinter import *
import curses

screen = curses.initscr()

curses.noecho()

curses.cbreak()

screen.keypad(True)

GPIO.setmode(GPIO.BOARD)

x = 7.5

GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7,50)
p.start(x)

try:
    while True:

        directionRequested = screen.getch()

        if directionRequested == curses.KEY_LEFT and x < 12.5:
            x+=0.5
            p.ChangeDutyCycle(x)

        elif directionRequested == curses.KEY_RIGHT and x > 2.5:
            x -= 0.5
            p.ChangeDutyCycle(x)

        elif directionRequested == curses.KEY_DOWN:
            x = 7.5
            p.ChangeDutyCycle(x)

        else:
            continue

except KeyboardInterrupt:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
