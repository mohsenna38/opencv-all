import cv2 as cv
import numpy as np
###############################################3
webcam = cv.VideoCapture(0)
while True:
	_,frame = webcam.read()
	hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	min = np.array([90,100,100])
	max = np.array([255,255,255])
	hsvbl = cv.inRange(hsv,min,max)
	fullblue = cv.bitwise_and(frame,frame,mask = hsvbl)
	cv.imshow('webcamhsv',fullblue)
	key = cv.waitKey(1)
	if  key == ord("q"):
		break
cv.destroyAllWindows()
