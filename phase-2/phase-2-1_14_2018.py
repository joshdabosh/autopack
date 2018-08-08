"""
p6 r21 wang joshua (ident)

GDoc for all sources for all phases:
https://docs.google.com/document/d/1LnDXlSY4a5JR0CGUkZy0pt4HscPgRDATz8VNCyvSxkU/edit?usp=sharing

"""

import RPi.GPIO as GPIO
import curses
import time
from threading import Thread

distances = []

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

    time.sleep(backTime)

    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)

def move(dist, char):
    if dist >= 10:
        if char == curses.KEY_UP:
            forward()

        elif char == curses.KEY_DOWN:
            backward()

        elif char == curses.KEY_LEFT:
            left()

        elif char == curses.KEY_RIGHT:
            right()

    else:
        backup(0.5)
            
def scan_for_obstacles():
    GPIO.setmode(GPIO.BOARD)
    while True:
        # tells the sensor to fire a burst of sound
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pass

        startTime = time.time()

        while GPIO.input(ECHO) == 1:
            pass

        stopTime = time.time()

        distance = (stopTime-startTime) * 17000

        distances.append(distance)

        time.sleep(0.025)

def Main():
    try:
        t1 = Thread(target = scan_for_obstacles)

        t1.start()

        while True:
            char = screen.getch()
            currDistance = distances[-1]
            
            t2 = Thread(target=move, args=(currDistance, char))

            t2.start()
            t2.join()
            
            
        
        
    finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()

if __name__ == '__main__':
    Main()
