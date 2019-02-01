import numpy as np
import cv2 as cv
##############################################################################################
webcam = cv.VideoCapture(0)
##############################################################################################
while(True):
    _,frame = webcam.read()
   #bluring the frame
    frame = cv.GaussianBlur(frame, (5, 5), 0)
   #color min max
    minbl= np.array([30,140,77])
    maxbl= np.array([255,255,255])
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
    #cv.imshow("edges", edges) 
    
    ikey = cv.waitKey(1)
    if(ord("q") == ikey):
        break
cv.destroyAllWindows()
 
