from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

x = 0

while x != 99:
    print "debug"
    camera.capture(rawCapture, format="bgr")
    print "debug1"
    image = rawCapture.array
    print "debug2"
    cv2.imshow("Image", image)
    print "debug3"
    rawCapture.truncate(0)
    print "debug4"
    x+=1
    print x
cv2.destroyAllWindows()
