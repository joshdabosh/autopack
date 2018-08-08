import RPi.GPIO as GPIO
import curses
import time

TRIG = 24
ECHO = 26

def move(char):
    if char == curses.KEY_UP:
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

    elif char == curses.KEY_DOWN:
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

    elif char == curses.KEY_LEFT:
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

    elif char == curses.KEY_RIGHT:
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

    elif char == 32:
        screen.addstr(0,0,'stop ')
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(12, False)
        GPIO.output(16, False)
        GPIO.output(18, False)
        GPIO.output(22, False)

    """
    else:
        screen.addstr(0,0, 'nuttin')
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(12, False)
        GPIO.output(16, False)
        GPIO.output(18, False)
        GPIO.output(22, False)
    """

    #char = ''

def backup():
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(12, False)
    GPIO.output(16, True)
    GPIO.output(18, False)
    GPIO.output(22, True)
    time.sleep(1)
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(12, False)
    GPIO.output(16, False)
    GPIO.output(18, False)
    GPIO.output(22, False)

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
GPIO.output(ECHO, False)

try:
    while True:

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        if GPIO.input(ECHO) == 1:

            startTime = time.time()

            while GPIO.input(ECHO) == 1:    # waits until the signal stops
                currTime = time.time()
                if currTime - startTime > 0.25:
                    break

                else:
                    pass                    # keeps going until one condition is
                                            # broken
            
            stopTime = time.time()

            distance = (stopTime - startTime) * 17000
            
        else:
            distance = 11

        char = screen.getch()

        if distance >= 10:

            move(char)

        else:
            backup()

finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
