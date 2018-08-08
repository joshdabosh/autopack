"""
p6 r21 wang joshua (ident)

GDoc for all sources for all phases:
https://docs.google.com/document/d/1LnDXlSY4a5JR0CGUkZy0pt4HscPgRDATz8VNCyvSxkU/edit?usp=sharing

"""

# ABANDONED IDEA

import RPi.GPIO as GPIO
import curses
import time
from threading import Thread

distance = 11

TRIG = 24
ECHO = 26

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

GPIO.setup(TRIG, GPIO.OUT)  # trigger voltage setup

GPIO.setup(ECHO, GPIO.IN)   # echo input setup

GPIO.output(7, False)       # set everything to false at startup
GPIO.output(11, False)
GPIO.output(13, False)
GPIO.output(15, False)
GPIO.output(12, False)
GPIO.output(16, False)
GPIO.output(18, False)
GPIO.output(22, False)
GPIO.output(TRIG, False)

def forward():
    screen.addstr(0,0, 'up   ')
    GPIO.output(7, False)           # makes sure that nothing else
    GPIO.output(11, False)          # is running when this runs
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(7, True)
    GPIO.output(13, True)
    GPIO.output(12, True)
    GPIO.output(18, True)

def backward():
    screen.addstr(0,0,'down ')
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(11, True)
    GPIO.output(15, True)
    GPIO.output(16, True)
    GPIO.output(22, True)

def left():
    screen.addstr(0,0,'left ')
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(11, True)
    GPIO.output(16, True)
    #GPIO.output(13, True)
    GPIO.output(18, True)

def right():
    screen.addstr(0,0, 'right')
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(7, True)
    GPIO.output(15, True)
    #GPIO.output(12, True)
    GPIO.output(22, True)

def stop():
    screen.addstr(0,0,'stop ')
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)

def backup(backTime):
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)

    GPIO.output(11, True)
    GPIO.output(15, True)
    GPIO.output(16, True)
    GPIO.output(22, True)

def move():
    while True:
        char = screen.getch()

        if char == curses.KEY_UP:
            forward()

        elif char == curses.KEY_DOWN:
            backward()

        elif char == curses.KEY_LEFT:
            left()

        elif char == curses.KEY_RIGHT:
            right()

        elif char == 32:
            stop()

def scan_for_obstacles():
    while True:
        # tells the sensor to fire a burst of sound
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        if GPIO.input(ECHO) == 1:

            start = time.time()

            while GPIO.input(ECHO) == 1:
                if time.time() - start > 0.25:
                    break
                else:
                    pass

            stop = time.time()

            global distance
            distance = (stop-start) * 17000

        else:
            global distance
            distance == 11

        return distance

def Main():
    try:
        scanner_thread = Thread(target=scan_for_obstacles)
        movement_thread = Thread(target=move)

        while True:
            if scanner_thread.start() >= 10:
                movemen
            
        
    finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()

if __name__ == '__main__':
    Main()
