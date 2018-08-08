import RPi.GPIO as GPIO
import time
import curses

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

GPIO.output(7, False)

x = 0

screen = curses.initscr()
curses.cbreak()
curses.noecho()
screen.keypad(True)

def move():
    GPIO.output(7, True)

def stop():
    GPIO.output(7, False)

def adder(x):
    return x+1

try:
    while True:
        x = adder(x)

        if x < 100:
            move()
            print 'ok'

        else:
            stop()
            print 'done'
except:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
