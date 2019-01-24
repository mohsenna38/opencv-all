import cv2 as cv
import numpy as np
#################################################################
def nothing(x):
    pass    
#################################################################
cv.namedWindow('track')
img = np.zeros((300,512,3),np.uint8)
#################################################################
cv.createTrackbar('red','track',0,255,nothing)
cv.createTrackbar('blue','track',0,255,nothing)
cv.createTrackbar('green','track',0,255,nothing)
#################################################################
while True:
    re = cv.getTrackbarPos('red','track')
    gr= cv.getTrackbarPos('green','track')
    bl = cv.getTrackbarPos('blue','track')
    img[:] = [bl,gr,re]
    cv.imshow('track',img)
#################################################################
    key = cv.waitKey(1)
    if ord("q") == key:
        break
cv.destroyAllWindows()
#################################################################        

