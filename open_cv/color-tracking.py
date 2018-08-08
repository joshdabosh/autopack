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


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 50
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
        image = frame.array

        blur = cv2.blur(image, (3,3))

        #hsv to complicate things, or stick with BGR
        #hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        #thresh = cv2.inRange(hsv,np.array((0, 200, 200)), np.array((20, 255, 255)))

        lower = np.array([3, 9, 114],dtype="uint8")
        upper = np.array([43, 49, 154], dtype="uint8")

        thresh = cv2.inRange(blur, lower, upper)
        thresh2 = thresh.copy()

        # find contours in the threshold image
        image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        # finding contour with maximum area and store it as best_cnt
        max_area = 0
        best_cnt = 1
        for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > max_area:
                        max_area = area
                        best_cnt = cnt

        # finding centroids of best_cnt and draw a circle there
        M = cv2.moments(best_cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        cv2.circle(blur,(cx,cy),10,(0,0,255),-1)

        # draws a line to the object
        cv2.line(blur,(cx,cy),((cx-25),(cy-25)),(0,0,255), 2)

        # finds the relative direction
        direction = find_dir(cx)

        # displays the location of the detected color
        cv2.putText(blur, ('{0}'.format(direction)), ((cx-30), (cy-30)), font, 0.8, (0,255,0), 2, cv2.LINE_AA)
        
        # show the frame
        cv2.imshow("Frame", blur)
        #cv2.imshow('thresh',thresh2)
        key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
        rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
        if key == ord("q"):
        	break
