import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import time as t
#############################################################
aks = cv.imread('dot.png')
cv.namedWindow('picture',cv.WINDOW_NORMAL)
cv.imshow('picture',aks)
cv.waitKey(0)
cv.destroyWindow('picture')

