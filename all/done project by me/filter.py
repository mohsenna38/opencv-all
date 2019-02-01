###############################################
import numpy as np
import cv2 as cv
###############################################
thing = cv.VideoCapture(0)
while(True):
    _,frame = thing.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    minbl= np.array([50,50,50])
    maxbl= np.array([255,255,255])
    smt = cv.inRange(hsv,minbl,maxbl)
    rand = cv.bitwise_and(frame,frame,mask = smt)
    cv.imshow('frame',rand)
    cv.imshow('smt',smt)
    a = cv.waitKey(1)
###############################################   
    if(ord("q") == a):
        break
cv.destroyAllWindows()
###############################################
