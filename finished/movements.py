import RPi.GPIO as GPIO
import time

class robot():
        def __init__(self):
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(7, GPIO.OUT)
                GPIO.setup(11, GPIO.OUT)
                
                GPIO.setup(13, GPIO.OUT)
                GPIO.setup(15, GPIO.OUT)
                
                GPIO.setup(12, GPIO.OUT)
                GPIO.setup(16, GPIO.OUT)
                
                GPIO.setup(18, GPIO.OUT)
                GPIO.setup(22, GPIO.OUT)

                GPIO.output(7, False)
                GPIO.output(11, False)
                
                GPIO.output(13, False)
                GPIO.output(15, False)
                
                GPIO.output(12, False)
                GPIO.output(16, False)
                
                GPIO.output(18, False)
                GPIO.output(22, False)


        def forward(self):
                GPIO.output(11, False)
                GPIO.output(15, False)
                GPIO.output(16, False)
                GPIO.output(22, False)
                
                GPIO.output(7, True)
                GPIO.output(13, True)
                GPIO.output(12, True)
                GPIO.output(18, True)


        def backward(self):
                GPIO.output(7, False)
                GPIO.output(13, False)
                GPIO.output(12, False)
                GPIO.output(18, False)
                
                GPIO.output(11, True)
                GPIO.output(15, True)
                GPIO.output(16, True)
                GPIO.output(22, True)


        def left_forward(self):
                GPIO.output(18, False)
                GPIO.output(15, False)
                GPIO.output(16, False)
                GPIO.output(22, False)
                GPIO.output(11, False)
                
                GPIO.output(7, True)
                GPIO.output(13, True)
                GPIO.output(12, True)


        def right_forward(self):
                GPIO.output(16, False)
                GPIO.output(15, False)
                GPIO.output(12, False)
                GPIO.output(22, False)
                GPIO.output(11, False)
                
                GPIO.output(7, True)
                GPIO.output(13, True)
                GPIO.output(18, True)


        def left(self):
                GPIO.output(7, False)
                GPIO.output(15, False)
                GPIO.output(12, False)
                GPIO.output(18, False)
                GPIO.output(22, False)
                
                GPIO.output(11, True)
                GPIO.output(16, True)
                GPIO.output(13, True)
                

        def right(self):
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(12, False)
                GPIO.output(16, False)
                GPIO.output(18, False)
                
                GPIO.output(7, True)
                GPIO.output(15, True)
                GPIO.output(22, True)


        def left_backward(self):
                GPIO.output(7, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
                GPIO.output(12, False)
                GPIO.output(18, False)
                
                GPIO.output(11, True)
                GPIO.output(16, True)
                GPIO.output(22, True)


        def right_backward(self):
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(12, False)
                GPIO.output(18, False)
                
                GPIO.output(15, True)
                GPIO.output(16, True)
                GPIO.output(22, True)

        def stop(self):
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
                GPIO.output(12, False)
                GPIO.output(16, False)
                GPIO.output(18, False)
                GPIO.output(22, False)

        def pause(self):
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
                GPIO.output(12, False)
                GPIO.output(16, False)
                GPIO.output(18, False)
                GPIO.output(22, False)

        def scan_for_obstacles(self):
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









