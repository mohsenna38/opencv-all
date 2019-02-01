##############################################################################################
import numpy as np
import cv2 as cv
##############################################################################################
window = 'frame'
cv.namedWindow(window)
webcam = cv.VideoCapture(1)
#################################################################
def nothing(x):
    pass    
#################################################################
cv.createTrackbar('hmin', window,0,255,nothing)
cv.createTrackbar('hmax', window,0,255,nothing)
cv.createTrackbar('smin', window,0,255,nothing)
cv.createTrackbar('smax', window,0,255,nothing)
cv.createTrackbar('vmin', window,0,255,nothing)
cv.createTrackbar('vmax', window,0,255,nothing)
cv.setTrackbarPos('hmax', window,255)
cv.setTrackbarPos('smax', window,255)
cv.setTrackbarPos('vmax', window,255)
##############################################################################################
while(True):
    _,frame = webcam.read()
   #bluring the frame
    frame = cv.GaussianBlur(frame, (5, 5), 0)
   
   #trackbar stuff 
    hmin = cv.getTrackbarPos('hmin',window)
    smin = cv.getTrackbarPos('smin',window)
    vmin = cv.getTrackbarPos('vmin',window)
    hmax = cv.getTrackbarPos('hmax',window)
    smax = cv.getTrackbarPos('smax',window)
    vmax = cv.getTrackbarPos('vmax',window)
   
   #color min max
    minbl = np.array([hmin, smin, vmin])
    maxbl = np.array([hmax, smax, vmax])
    #minbl= np.array([30,140,77])
    #maxbl= np.array([255,255,255])
   #hsv converter
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
   
   #frame to binary frame
    binaried = cv.inRange(hsv,minbl,maxbl)
   
   #removing the noise spots
    medianed = cv.medianBlur(binaried, 25) 

   #finding the edge lines
    edges = cv.Canny(medianed, 75, 120)

   #getting the edge of lines
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)

   #getting the cordinants of lines
    try:
        if (len(lines) > 0):
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        print(" x1 is: ",x1," y1 is: ",y1," x2 is: ",x2," y2 is: ",y2)
   
    except:
        print("nothing found")

   #showing some stuff
    cv.imshow("frame", frame)
    cv.imshow("edges", edges)
    cv.imshow("hsv", hsv)
###############################################   
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        cv.destroyAllWindows()
        break
 
