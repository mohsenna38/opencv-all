from math import *
def hesab(l1,l2,tt1,tt2):
    xe = l1*cos(tt1)+l2*cos(tt1+tt2)
    ye = l1*sin(tt1)+l2*sin(tt1+tt2)
    print("xe = ",xe)
    print("ye = ",ye)
l1 = float(input("andaze ye bazo1"))
l2 = float(input("andaze ye bazo2"))
tt1 = radians(float(input("zavie 1")))
tt2 = radians(float(input("zavie 2")))
hesab(l1,l2,tt1,tt2)
