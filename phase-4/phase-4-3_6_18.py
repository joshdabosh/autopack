from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import cv2
import numpy as np
import movements
import time

def find_dir(x):
        x_cent = 320
        
        if x > x_cent:
                direction = 'right'
                dist_from_cent = x-x_cent

        elif x == x_cent:
                direction = 'center'
                dist_from_cent = 0

        else:
                direction = 'left'
                dist_from_cent = x_cent-x

        return direction, dist_from_cent


def main():
        robot = movements.robot()
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 50
        camera.hflip = True

        rawCapture = PiRGBArray(camera, size=(640, 480))
         
        time.sleep(0.1)

        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                image = frame.array

                blur = cv2.GaussianBlur(image, (3,3), 0)

                lower = np.array([3, 9, 114],dtype="uint8")
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

                direction, distance_from_cent = find_dir(cx)
                
                if detected == True:
                        scan_dist = robot.scan_for_obstacles()

                        if scan_dist >= 25:
                                if direction == 'left':
                                        robot.left_forward()

                                elif direction == 'right':
                                        robot.right_forward()

                                robot.pause()

                        elif scan_dist >= 10:
                                if direction == 'left':
                                        robot.left()

                                elif direction == 'right':
                                        robot.right()

                                else:
                                        robot.pause()

                        else:
                                if direction == 'left':
                                        robot.left_backward()

                                elif direction == 'right':
                                        robot.right_backward()

                                else:
                                        robot.pause()
                        
                else:
                        robot.pause()

                rawCapture.truncate(0)
                

if __name__ == '__main__':
        GPIO.setmode(GPIO.BOARD)

        TRIG = 24
        ECHO = 26

        font = cv2.FONT_HERSHEY_SIMPLEX
        
        main()



