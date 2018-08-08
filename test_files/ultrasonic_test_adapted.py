import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 24
ECHO = 26

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

while True:
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
        distance = 11

    print distance

GPIO.cleanup()
