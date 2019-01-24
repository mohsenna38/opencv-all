from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2 as cv

#tabe nevisi XD
def webcamseting(fps):
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = fps
    rawCapture = PiRGBArray(camera, size=(640, 480))
  