#################################################################
import numpy as np
import cv2 as cv
#################################################################
webcam = cv.VideoCapture(0)
while True:
    _,frame = webcam.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#################################################################
    #blue = min: [90, 100, 100] max: [150 255, 255]
    #red = min:[130, 130, 100] max: [255, 255, 255]
    #blue and red = min: [100, 130, 150] max:[255, 255, 255]
    minr = np.array([130, 130, 100])
    maxr = np.array([255, 255, 255])
    minb = np.array([90, 100, 100])
    maxb = np.array([150, 255, 255])
    redp = cv.inRange(hsv, minr, maxr)
    bluep = cv.inRange(hsv, minb, maxb)
    bluepic = cv.bitwise_and(frame, frame, mask=bluep )
    redpic = cv.bitwise_and(frame, frame, mask=redp )
    realpic = cv.bitwise_or(redpic,bluepic)
#################################################################
    cv.imshow('red',redpic)
    cv.imshow('blue',bluepic)
    cv.imshow('real',realpic)

#################################################################
    a = cv.waitKey(1)
    if ord("q") == a:
        break
cv.destroyAllWindows()
#################################################################