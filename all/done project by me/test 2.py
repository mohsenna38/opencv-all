import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import miangin
from statistics import mean
#############################################################
aks1 = Image.open('y0.5.png')
im1 = np.asarray(aks1)
im1.setflags(write=1)
jav = miangin.arraymin(im1)
lenA = len(im1)
lenB = len(im1[0])
lenC = len(im1[0][0])
#############################################################
for n in range (0 ,lenA):
        for x in range(0,lenB):
                imavg = mean(im1[n][x][:3])
                if (jav > imavg):
                        for z in range (0,lenC - 1):
                                im1[n][x][z] = 255
                if (jav < imavg):
                        for z in range (0,lenC - 1):
                                im1[n][x][z] = 0
print(im1)

plt.imshow(im1)
plt.show()

