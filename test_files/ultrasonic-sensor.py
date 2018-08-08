import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 24
ECHO = 26

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)

time.sleep(0.1)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        print 'sent out trigger signal'

        while GPIO.input(ECHO) == 0:
            #print 'debug'
            pass

        start = time.time()

        while GPIO.input(ECHO) == 1:
            pass

        stop = time.time()

        print (stop-start) * 17000
        time.sleep(0.5)
        print 'ok'
        
except:
    GPIO.cleanup()

print 'finished'
