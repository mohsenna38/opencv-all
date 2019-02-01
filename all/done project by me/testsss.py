###############################################
import numpy as np
import cv2 as cv
###############################################
thing = cv.VideoCapture(0)
while(True):
    _,frame = thing.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    minbl= np.array([110,50,50])
    maxbl= np.array([130,255,255])
    smt = cv.inRange(hsv,minbl,maxbl)
    cv.imshow('picture',hsv)
    cv.imshow('frame',frame)
    cv.imshow('smt',smt)
    a = cv.waitKey(1)
###############################################   
    if(ord("q") == a):
        break
cv.destroyAllWindows()
###############################################
