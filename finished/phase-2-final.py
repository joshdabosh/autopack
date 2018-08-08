import RPi.GPIO as GPIO
import time

TRIG = 24
ECHO = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)     # motor 1, forward, top right
GPIO.setup(13, GPIO.OUT)    # motor 2, forward, top left
GPIO.setup(12, GPIO.OUT)    # motor 3, forward, bottom right
GPIO.setup(18, GPIO.OUT)    # motor 4, forward, botton left

GPIO.setup(TRIG, GPIO.OUT)  # trigger voltage setup

GPIO.setup(ECHO, GPIO.IN)   # echo input setup

GPIO.output(7, False)       # set everything to false at startup
GPIO.output(13, False)
GPIO.output(12, False)
GPIO.output(18, False)

GPIO.output(TRIG, False)
            
def scan_for_obstacles():
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

    return distance


GPIO.output(7, True)
GPIO.output(13, True)
GPIO.output(12, True)
GPIO.output(18, True)

try:
    while True:
        if scan_for_obstacles() <= 10:
            GPIO.output(7, False)
            GPIO.output(13, False)
            GPIO.output(12, False)
            GPIO.output(18, False)
            break

        else:
            continue

finally:
    GPIO.cleanup()











