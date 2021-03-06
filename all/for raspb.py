import time
import cv2 as cv
import numpy as np
from imutils.video import VideoStream
import imutils
###################################################################################################################################### 
#to see if camera is connected 
usingPiCamera = True
frameSize = (320, 240)
######################################################################################################################################
# mutithreading the video playback
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
		framerate=60).start()
######################################################################################################################################
#warming up the camera
time.sleep(2.0)
######################################################################################################################################
while True:
	frame = vs.read()
	if not usingPiCamera:
		frame = imutils.resize(frame, width=frameSize[0])
   #center of frames
    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)

   #hsv converting
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

   #filter array
    minf = np.array([170,55,65])
    maxf = np.array([255,255,255])

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
            ajwnfaojfnm + 3
        else:
            errx = mrkzx - cntx
            erry = mrkzy - cnty
           
           #servo stuff
            dtx = errx / 640
            dty = erry / 640

           #dtx to 0.01
            dtx = (int(dtx*10))/10
            dty = (int(dty*10))/10

           #dtx go left or right
            if (dtx >= 0):
                servx = np.arange(dt2,dt2 + 2*dtx,dtx)
                dt2 = dt2 + 2*dtx
            elif (dtx <= 0):
                dtx = -dtx
                servx = np.arange(dt2 - 2*dtx,dt2,dtx)
                dt2 = dt2 - 2*dtx
            if (dty >= 0):
                servy = np.arange(dt1,dt1 + dty,dty)
                dt1 = dt1 + dty
            elif (dty <= 0):
                dty = -dty
                servy = np.arange(dt1 - dty,dt1,dty)
                dt1 = dt1 - dty
           #timing
            timex = (int(map(dtx,320,0,0,1)*10))/10
            timey = (int(map(dty,320,0,0,1)*10))/10
                
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

   #not finding any contour
    except Exception as excerr:
        print(excerr)
        if ("name 'ajwnfaojfnm' is not defined" == str(excerr)):
            print("nothing found")
            dt2 = dt2 + 1
            if (dt2 >= 11):
                dt2 = 2
                dt1 = dt1 + 0.5
                if (dt1 >= 6):
                        dt1 = 2
            pwm1.ChangeDutyCycle(dt1)
            pwm2.ChangeDutyCycle(dt2)

   #show stuff
    cv.imshow('frame',frame)

   #close stuff
    ikey = cv.waitKey(5)
    video.truncate(0)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        pwm1.stop()
        pwm2.stop()
        rp.cleanup()
        vs.stop()
        break