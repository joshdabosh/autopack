from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import cv2
import numpy as np
import movements
import time

def find_pos(x):
    x_cent = 320
    if x > x_cent:
            direction = 'right'

    else:
            direction = 'left'

    return direction

def main():
    robot = movements.robot()
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 50
    camera.hflip = True
    camera.vflip = True

    counter1 = 0

    rawCapture = PiRGBArray(camera, size=(640, 480))

    time.sleep(0.1)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        blur = cv2.GaussianBlur(image, (3,3), 0)

        lower = np.array([3,9,114], dtype="uint8")
        upper = np.array([43, 49, 154], dtype="uint8")

        thresh = cv2.inRange(blur, lower, upper)
        thresh2 = thresh.copy()

        image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        max_area = 0
        best_cent = 1
        detected = False
        for cent in contours:
            area = cv2.contourArea(cent)
            if area > max_area:
                max_area = area
                best_cent = cent
                detected = True

        M = cv2.moments(best_cent)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(blur,(cx,cy),10,(0,0,255), -1)

        cv2.imshow('Tracking', blur)
        
        direction = find_pos(cx)
        if detected == True:
            print '{}'.format(direction)

            if direction == 'left':
                robot.left_forward()

            else:
                robot.right_forward()

        else:
            print 'nuttin'
            robot.pause()

        blah = cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if blah == ord("q"):
            break

if __name__ == '__main__':
    main()
    GPIO.cleanup()
