import RPi.GPIO as GPIO
import time
from threading import Thread

distances = []

TRIG = 24
ECHO = 26

GPIO.setmode(GPIO.BOARD)

GPIO.setup(TRIG, GPIO.OUT)  # trigger voltage setup

GPIO.setup(ECHO, GPIO.IN)   # echo input setup

GPIO.output(TRIG, False)

distances = []

def scan_for_obstacles():
    GPIO.setmode(GPIO.BOARD)
    while True:
        GPIO.setmode(GPIO.BOARD)
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

def move():
    dist = distances[-1]
    if dist <= 10:
        print 'uh oh a-somebody toucha mah spagheett'

def Main():
    try:
        t1 = Thread(target = scan_for_obstacles)

        t1.start()
            
        t2 = Thread(target=move)

        t2.start()
        t2.join()

        print distances
            
            
        
        
    except KeyboardInterrupt:
        # shut down cleanly
        GPIO.cleanup()

if __name__ == '__main__':
    Main()
