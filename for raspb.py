import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv
import RPi.GPIO as rp
from time import sleep

servo1 = 21
servo2 = 20
dt1 = 7
dt2 = 7
rp.setmode(rp.BCM)
rp.setwarnings(False)
rp.setup(servo1,rp.OUT)
rp.setup(servo2,rp.OUT)
pwm1 = rp.PWM(servo1,50)
pwm2 = rp.PWM(servo2,50)
pwm1.start(4)
pwm2.start(7)

webcam = PiCamera()
webcam.resolution = (640,480)
webcam.framerate = 30
video = PiRGBArray(webcam,size=(640,480))

for frames in webcam.capture_continuous(video, format="bgr", use_video_port=True):
    
    frame = frames.array

    mrkzy = int(len(frame)/2)
    mrkzx = int(len(frame[0])/2)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    minf = np.array([100,50,50])
    maxf = np.array([145,255,255])

    binary = cv.inRange(hsv, minf, maxf)
    medianed = cv.medianBlur(binary, 25)  

    filterd = cv.bitwise_and(frame,frame, mask= medianed)
    im2, contours, hierarchy = cv.findContours(medianed,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)  
    if len(contours) > 0:
        cnt = max(contours, key = cv.contourArea)
        (x1,y1), radius=cv.minEnclosingCircle(cnt)
        cntx = int(x1)  
        cnty = int(y1)
        center = (int(x1),int(y1))
        radius = int(radius)
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.circle(frame,center,radius,(0,0,255),2)
        cv.circle(frame,center,2,(255,0,0),4) 

    if(mrkzy > cnty):
        dt1 = dt1 + 0.3
        print("kaley robot be samt (bala) nega kon")
    elif(mrkzy < cnty):
        dt1 = dt1 - 0.3
        print("kaley robot be samt (paen) nega kon")
    elif(mrkzy == cnty):
        print("kaley robot stop")
    if(mrkzx > cntx):
        dt2 = dt2 + 0.3
        print("kaley robot be samt (chap) nega kon")
    elif(mrkzx < cntx):
        dt2 = dt2 - 0.3
        print("kaley robot be samt (rast) nega kon")
    elif(mrkzx == cntx):
        print("kaley robot stop")
    if (dt1 <= 2):
        dt1 = 2
    elif (dt1 >= 12):
        dt1 = 12
    if (dt2 <= 2):
        dt2 = 2
    elif (dt2 >= 12):
        dt2 = 12
    pwm1.ChangeDutyCycle(dt1)
    pwm2.ChangeDutyCycle(dt2)
        
    cv.imshow('frame',frame)
    cv.imshow('filtered',filterd)
    ikey = cv.waitKey(5)
    video.truncate(0)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        pwm1.stop()
        pwm2.stop()
        rp.cleanup()
        break
