# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# set the text font
font = cv2.FONT_HERSHEY_SIMPLEX

# set the center of the frame for x and y
x_cent = 320
y_cent = 240


# determine the relative position the detected point is at to the camera
def find_dir(x):
        if x > x_cent:
                direction = 'right'

        else:
                direction = 'left'

        return direction

# init the camera and start using the camera stream
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 50
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        blur = cv2.GaussianBlur(image, (3,3), 0)

        lower = np.array([3, 9, 114],dtype="uint8")
        upper = np.array([43, 49, 154], dtype="uint8")

        thresh = cv2.inRange(blur, lower, upper)
        thresh2 = thresh.copy()

        # detect contours
        image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        # find largest area that's different from surroundings and assign it to best_cent
        max_area = 0
        best_cent = 1
        for cent in contours:
                area = cv2.contourArea(cent)
                if area > max_area:
                        max_area = area
                        best_cent = cent

        # draws a circle from the top to the center of the circle
        M = cv2.moments(best_cent)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.circle(blur,(cx,cy),10,(0,0,255),-1)

        # draws a line to the object
        cv2.line(blur,(cx,cy),((cx-25),(cy-25)),(0,0,255), 2)

        # finds the relative direction
        direction = find_dir(cx)

        # displays the location of the detected color
        cv2.putText(blur, ('{0}'.format(direction)), ((cx-30), (cy-30)), font, 0.8, (0,255,0), 2, cv2.LINE_AA)
        
        # show the frame
        cv2.imshow('Tracking', blur)

        # waits for an input for 1 milisecond; if none, keep going
        key = cv2.waitKey(1) & 0xFF
 
	# get ready to display the next frame
        rawCapture.truncate(0)
 
	# detect when to stop
        if key == ord("q"):
        	break

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)








