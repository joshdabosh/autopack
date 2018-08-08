#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(7, False)
GPIO.output(11, False)
GPIO.output(12, False)
GPIO.output(13, False)
GPIO.output(15, False)
GPIO.output(16, False)
GPIO.output(18, False)
GPIO.output(22, False)
GPIO.output(24, False)
GPIO.output(26, False)

GPIO.cleanup()
