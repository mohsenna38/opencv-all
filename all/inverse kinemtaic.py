from matplotlib.pyplot import *
from math import *
from numpy import *
###########################################################################
l1 = float(input("andaze yeye bazo1  "))
l2 = float(input("andaze yeye bazo2  "))
xe = float(input("noghte xe:  "))
ye = float(input("noghte ye:  "))
###########################################################################
def hesab1(l1,l2,xe,ye):
    tt2 = arccos(((xe**2)+(ye**2)-(l1**2)-(l2**2))/((2*l1*l2)))
    tt1 = atan2(ye,xe)-atan2(l2*sin(tt2),l1+l2*cos(tt2))
    print("tt1 = ",tt1)
    print("tt2 = ",tt2)

###########################################################################
hesab1(l1,l2,xe,ye)

