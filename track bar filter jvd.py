import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
hn,sn,vn = 0,0,0
hx,sx,vx = 0,0,0
# Creating track bar
cv2.createTrackbar('hn', 'result',0,255,nothing)
cv2.createTrackbar('sn', 'result',0,255,nothing)
cv2.createTrackbar('vn', 'result',0,255,nothing)
cv2.createTrackbar('hx', 'result',0,255,nothing)
cv2.createTrackbar('sx', 'result',0,255,nothing)
cv2.createTrackbar('vx', 'result',0,255,nothing)

while(1):

    _, frame = cap.read()

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    hn = cv2.getTrackbarPos('hn','result')
    hx = cv2.getTrackbarPos('hx','result')
    vn = cv2.getTrackbarPos('vn','result')
    vx = cv2.getTrackbarPos('vx','result')
    sn = cv2.getTrackbarPos('sn','result')
    sx = cv2.getTrackbarPos('sx','result')

    # Normal masking algorithm
    lower_blue = np.array([hn,sn,vn])
    upper_blue = np.array([hx,sx,vx])
    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
