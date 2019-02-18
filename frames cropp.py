import numpy as np
import cv2 as cv

webcam = cv.VideoCapture(0)
###################################
while(True):
    _,frame = webcam.read()
##################
    cropped1 = frame[0:480, 0:160]
    cropped2 = frame[0:480, 480:640]
    cropped3 = frame[0:120, 0:640]
    cropped4 = frame[360:480, 0:640]
##################
    cv.imshow("cropped1", cropped1)
    cv.imshow("cropped2", cropped2)
    cv.imshow("cropped3", cropped3)
    cv.imshow("cropped4", cropped4)
    cv.imshow("frame", frame)
###################################
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
 
