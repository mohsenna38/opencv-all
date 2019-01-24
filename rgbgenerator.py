import cv2 as cv
import numpy as np
#################################################################
def nothing(x):
    pass    
cv.namedWindow('window')
img = np.zeros((300,512,3),np.uint8)
#################################################################
cv.createTrackbar('r', 'window',0,255,nothing)
cv.createTrackbar('g', 'window',0,255,nothing)
cv.createTrackbar('b', 'window',0,255,nothing)
#################################################################
while True:
#################################################################
    rm = cv.getTrackbarPos('r','window')
    gm = cv.getTrackbarPos('g','window')
    bm = cv.getTrackbarPos('b','window')
#################################################################
    img[:] = [bm,gm,rm]
    cv.imshow('window',img)
#################################################################
    ikey = cv.waitKey(1)
    if ord("q") == ikey:
        break
cv.destroyAllWindows()
#################################################################
