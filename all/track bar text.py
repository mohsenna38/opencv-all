import cv2 as cv
import numpy as np
#################################################################
def nothing(x):
    pass    
#################################################################
webcam = cv.VideoCapture(0)
cv.namedWindow('track')
#################################################################
cv.createTrackbar('sj','track',0,255,nothing)
cv.createTrackbar('mn','track',0,255,nothing)
cv.createTrackbar('al','track',0,255,nothing)
cv.createTrackbar('ma','track',0,255,nothing)
#################################################################
while True:
    _,frame = webcam.read()
    saj = cv.getTrackbarPos('sj','track')
    moh = cv.getTrackbarPos('mn','track')
    ali = cv.getTrackbarPos('al','track')
    mar = cv.getTrackbarPos('ma','track')
    cv.putText(frame,str(mar),(200,500),cv.FONT_HERSHEY_COMPLEX, 4,(ali,saj,moh),2,cv.LINE_AA)
    cv.imshow('track',frame)
#################################################################
    key = cv.waitKey(1)
    if ord("q") == key:
        break
cv.destroyAllWindows()
#################################################################        

