####################################################################################################### intruduction
#in code tamame dastoraee has ke ostad ta alan darbareye opencv gofte va ...
#in code ejraee nis faghat ye list az inja copy knin baray rahati 
#by Mohsen ^_^
####################################################################################################### libraries needed
import numpy as np
import cv2 as cv
import matplotlib as plt
####################################################################################################### images
cap = cv.VideoCapture(0)
aks1 = cv.imread('dot.png')
img = np.zeros((300,512,3),np.uint8)
img2 = np.zeros((480,640,3), np.uint8) #used with contours by ostad setayeshi
####################################################################################################### displayers
plt.imshow(aks1)
plt.show()
cv.imshow('window',img)
####################################################################################################### to np array
_,frame = cap.read()
####################################################################################################### color format
revclr = cv.cvtColor(aks1,cv.COLOR_BGR2RGB)
####################################################################################################### windows maker
cv.namedWindow('picture',cv.WINDOW_NORMAL)
cv.namedWindow('track')
####################################################################################################### interupt and close
cv.waitKey(0)
cv.destroyAllWindows()
cv.destroyWindow('picture')
ord("")
cap.release()
###########################
ikey = cv.waitKey(1)
if ord("q") == ikey:
    break
cv.destroyAllWindows()
####################################################################################################### binary filter
minbl= np.array([110,50,50])
maxbl= np.array([130,255,255])
mask = cv.inRange(pic,minimum,maximum)
####################################################################################################### betwise
RES = cd.bitwise_and(frame,frame,mask = mask)
realpic = cv.bitwise_or(redpic,bluepic)
####################################################################################################### stuff dispaly on pic
cv.putText(frame,str(saj),(200,500),cv.FONT_HERSHEY_COMPLEX, 4,(0,0,255),2,cv.LINE_AA)
x,y,w,h = cv.boundingRect(cnt)
frame = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
(x1,y1), radius=cv.minEnclosingCircle(cnt)
center = (int(x1),int(y1))
radius = int(radius)
cv.circle(frame,center,radius,(0,0,255),2)
cv.circle(frame,center,2,(255,0,0),4)
####################################################################################################### trackbars
def nothing(x):
    pass  
cv.createTrackbar('red','track',0,255,nothing)
cv.setTrackbarPos('hmax', 'window',255)
re = cv.getTrackbarPos('red','track')
####################################################################################################### removing binarry pic errs
madian = cv.medianBlur(mask, 15)
####################################################################################################### contour
im2, contours, hierarchy = cv.findContours(madian,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
area = cv.contourArea(cnt)
cnt = max(contours, key = cv.contourArea)
cv.drawContours(frame, contours, -1, (0,255,0), 3)
####################################################################################################### center of all frames
mrkzy = int(len(frame)/2)
mrkzx = int(len(frame[0])/2)