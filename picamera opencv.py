#######################################################################################################################################
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image on screen and wait for a keypress
cv.imshow("Image", image)
cv.waitKey(0)`

#######################################################################################################################################
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv

webcam = PiCamera()
webcam.resolution = (640,480)
webcam.framerate = 30
video = PiRGBArray(webcam,size=(640,480))
  
for frames in webcam.capture_continuous(video, format="bgr", use_video_port=True):
    frame = frames.array


    ikey = cv.waitKey(5)
    video.truncate(0)
    if (ikey==ord("q")):
        cv.destroyAllWindows()
        break
