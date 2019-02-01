import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from statistics import mean
def arraymin(A):
###############################################################################
    lenA = len(A)
    lenB = len(A[0])
    lenC = len(A[0][0])
    rgbmean = []
    a = []
    b = []
    c = []
    d = []
    f = []
    ma = 0
    mb = 0
    mc = 0
    md = 0
###############################################################################
    for n in range (0 ,lenA):
        for x in range(0,lenB):
            rgbmean = mean(x[:3])
            print(rgbmean)
'''
###############################################################################
    lenD = len(a)
    for y in range(0,lenD):    
        ma = ma + a[y]
        mb = mb + b[y]
        mc = mc + c[y]
        md = md + d[y]
    f = f + [int(ma/lenD)] + [int(mb/lenD)] + [int(mc/lenD)] + [int(md/lenD)]
###############################################################################
    for l in
###############################################################################
    return (f)'''
arraymin([[[[250, 237, 55, 255]],[250, 237, 55, 255],[250, 237, 55, 255]],[[[250, 237, 55, 255]],[250, 237, 55, 255],[250, 237, 55, 255]]]);             
