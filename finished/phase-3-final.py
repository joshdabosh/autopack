from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

x_cent = 320
y_cent = 240

def find_dir(x):
        if x > x_cent:
                direction = 'right'

        else:
                direction = 'left'

        return direction

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 50
camera.hflip = True
camera.vflip= True

rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        blurredImage = cv2.GaussianBlur(image, (3,3), 0)
        orig = blurredImage.copy()

        lower = np.array([0, 6, 111],dtype="uint8")
        upper = np.array([53, 59, 164], dtype="uint8")

        thresh = cv2.inRange(blurredImage, lower, upper)
        thresh2 = thresh.copy()

        image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        max_area = 0
        best_cent = 1
        for cent in contours:
                area = cv2.contourArea(cent)
                if area > max_area:
                        max_area = area
                        best_cent = cent

        M = cv2.moments(best_cent)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(blurredImage,(cx,cy),10,(255,0,0),-1)

        cv2.line(blurredImage,(cx,cy),((cx-25),(cy-25)),(0,0,255), 2)

        direction = find_dir(cx)

        cv2.putText(blurredImage, ('{0}'.format(direction)), ((cx-30), (cy-30)), font, 0.8, (0,255,0), 2, cv2.LINE_AA)

        cv2.imshow('Input', orig)

        cv2.imshow('Orange detection', thresh)

        cv2.imshow('Output', blurredImage)

        key = cv2.waitKey(1) & 0xFF

        rawCapture.truncate(0)

        if key == ord("q"):
        	break

        elif key == ord("d"):
                cv2.imwrite('input.png', orig)
                cv2.imwrite('detect.png', thresh)
                cv2.imwrite('output.png', blurredImage)

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
