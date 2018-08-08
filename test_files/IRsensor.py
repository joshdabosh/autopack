import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

#take in input from the sensor thing

try:
    while True:

        sensor = GPIO.input(11) # Make sure it's included in the loop so that
                                # every iteration of the loop, it rereads the input
        
        if sensor==0:           # detected something
            print('stopping')
            sleep(1)

        elif sensor==1:         # detected nothing
            print('nuttin\'')

except KeyboardInterrupt:
    GPIO.cleanup()
