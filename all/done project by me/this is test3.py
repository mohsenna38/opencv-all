import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import time as t
#############################################################
aks1 = cv.imread('dot.png')
#print(type(aks1))
#plt.imshow(aks1)
#plt.show()
revclr = cv.cvtColor(aks1,cv.COLOR_BGR2RGB)
cv.namedWindow('picture',cv.WINDOW_NORMAL)
cv.imshow('picture',revclr)
cv.waitKey(0)
cv.destroyALLWindows()

