from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv

webcam = PiCamera()
webcam.resolution = (640,480)
webcam.framerate = 30
video = PiRGBArray(webcam,size=(640,480))

def nothing(x):
    pass    
cv.namedWindow('window',cv.WINDOW_FREERATIO)
#################################################################
cv.createTrackbar('hmin', 'window',0,255,nothing)
cv.createTrackbar('hmax', 'window',0,255,nothing)
cv.createTrackbar('smin', 'window',0,255,nothing)
cv.createTrackbar('smax', 'window',0,255,nothing)
cv.createTrackbar('vmin', 'window',0,255,nothing)
cv.createTrackbar('vmax', 'window',0,255,nothing)
cv.setTrackbarPos('hmax', 'window',255)
cv.setTrackbarPos('smax', 'window',255)
cv.setTrackbarPos('vmax', 'window',255)
  
for frames in webcam.capture_continuous(video, format="bgr", use_video_port=True):
    frame = frames.array

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#################################################################
    hmin = cv.getTrackbarPos('hmin','window')
    smin = cv.getTrackbarPos('smin','window')
    vmin = cv.getTrackbarPos('vmin','window')
    hmax = cv.getTrackbarPos('hmax','window')
    smax = cv.getTrackbarPos('smax','window')
    vmax = cv.getTrackbarPos('vmax','window')
#################################################################
    minfr = np.array([hmin, smin, vmin])
    maxfr = np.array([hmax, smax, vmax])
    moz = cv.inRange(hsv, minfr, maxfr)
    mooz = cv.bitwise_and(frame, frame, mask=moz )
#################################################################
    cv.imshow('window',mooz)

    ikey = cv.waitKey(5)
    video.truncate(0)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        break
