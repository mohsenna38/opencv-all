import numpy as np
import cv2 as cv
thing = cv.VideoCapture(0)
while(True):
    _,frame = thing.read()
    cv.imshow('frame',frame)
    a = cv.waitKey(1)
    if(ord("q") == a):
        break
cv.destroyAllWindows()
