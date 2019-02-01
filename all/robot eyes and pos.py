from imutils.video import VideoStream
import imutils
import numpy as np
import cv2 as cv
import RPi.GPIO as rp
from time import sleep
#################################################################################################################################
def map( x, in_min,in_max, out_min, out_max):
    maps = -((x - in_max)*(out_max-out_min)/(in_max-in_min)+out_min)
    return maps
#################################################################################################################################
#def nothing(x):
#    pass    
#cv.namedWindow('window')
#cv.createTrackbar('ksaad', 'window',1,100000,nothing)
#cv.createTrackbar('ktime','window',1,1000,nothing)
kti = 10
ksa = 1000
#################################################################################################################################
servo1 = 15
servo2 = 14
deltadt = 0.1
dt1 = 4
dt2 = 6
#################################################################################################################################
rp.setmode(rp.BCM)
rp.setwarnings(False)
rp.setup(servo1,rp.OUT)
rp.setup(servo2,rp.OUT)
pwm1 = rp.PWM(servo1,50)
pwm2 = rp.PWM(servo2,50)
pwm1.start(2)
pwm2.start(6)
#################################################################################################################################
cv.namedWindow('frame',cv.WINDOW_FREERATIO)
usingPiCamera = True
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=(240, 240),
	framerate=60).start()
#wait for camera to load1
sleep(0.2)
################################################################################################################################	
while True:
   #frame reading n stuff
    frame = vs.read()
    if not usingPiCamera:
	    frame = imutils.resize(frame, width=frameSize[0])

   #trackbar for servo noise	    
    #kti = cv.getTrackbarPos('ktime','window')
    #ksa = cv.getTrackbarPos('ksaad','window')  

   #center of frames
    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)
    fry = int(len(frame))
    frx = int(len(frame[0]))

   #filter array
    minf = np.array([100,110,0])
    maxf = np.array([125,255,255])

   #hsv converting
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

   #binaried frames
    binary = cv.inRange(hsv, minf, maxf)
    medianed = cv.medianBlur(binary, 25)  

   #contouring
    filterd = cv.bitwise_and(frame,frame, mask= medianed)
    im2, contours, hierarchy = cv.findContours(medianed,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

   #countor cordinants
    try:
        (x1,y1) = (0,0)
        cntx = 9999  
        cnty = 9999
   
   #countor cordinants and circling 
        if len(contours) > 0:
            cnt = max(contours, key = cv.contourArea)
            (x1,y1), radius=cv.minEnclosingCircle(cnt)
            center = (int(x1),int(y1))
            radius = int(radius)
            x,y,w,h = cv.boundingRect(cnt)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv.circle(frame,center,radius,(0,0,255),2)
            cv.circle(frame,center,2,(255,0,0),4)
            cntx = int(x1)  
            cnty = int(y1)
        if(cntx == 9999 or cnty == 9999):
            notfound + 3
        else:
            errx = mrkzx - cntx
            erry = mrkzy - cnty
           
           #servo stuff
            dtx = errx / (frx*2)
            dty = erry / (fry*2)

           #dtx to 0.01
            dtx = (int(dtx*ksa))/ksa
            dty = (int(dty*ksa))/ksa

           #timing
            timex = (int(map(dtx,mrkzx,0,0,1)*kti))/kti
            timey = (int(map(dty,mrkzy,0,0,1)*kti))/kti

           #dtx go left or right
            if (dtx >= 0):
                servx = np.arange(dt2,dt2 + dtx,dtx)
                dt2 = dt2 + dtx
            elif (dtx <= 0):
                dtx = -dtx
                servx = np.arange(dt2 - dtx,dt2,dtx)
                dt2 = dt2 - dtx
            if (dty >= 0):
                servy = np.arange(dt1,dt1 + dty,dty)
                dt1 = dt1 + dty
            elif (dty <= 0):
                dty = -dty
                servy = np.arange(dt1 - dty,dt1,dty)
                dt1 = dt1 - dty
                
           #if to pervent dt's going below or above the limits  
            if (dt1 <= 2.5):
                dt1 = 2.5
            elif (dt1 >= 11):
                dt1 = 11
            if (dt2 <= 2.5):
                dt2 = 2.5
            elif (dt2 >= 11):
                dt2 = 11
            
           #moving twords contour
            for f in servx:
                pwm2.ChangeDutyCycle(f)
                sleep(timex)
            for u in servy:
                pwm1.ChangeDutyCycle(u)
                sleep(timey)
            xposservo = (int(f*10)/1)
            xposservo = (int(u*10)/1)
   #not finding any contour
    except Exception as excerr:
        print(excerr)
        if ("name 'notfound' is not defined" == str(excerr)):
            print("nothing found")
            dt2 = dt2 + 1
            if (dt2 >= 11):
                dt2 = 2
                dt1 = dt1 + 0.5
                if (dt1 >= 6):
                        dt1 = 2
            pwm1.ChangeDutyCycle((int(dt1*10)/10))
            pwm2.ChangeDutyCycle((int(dt2*10)/10))
        elif("float division by zero" == str(excerr)):
            print("servostop")
            #servo must pause here

   #show stuff
    cv.imshow('frame',frame)
    print((int(dt1*10)/10),(int(dt2*10)/10))
   #close stuff
    ikey = cv.waitKey(5)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        pwm1.stop()
        pwm2.stop()
        rp.cleanup()
        vs.stop()
        break
