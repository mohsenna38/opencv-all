from matplotlib.pyplot import *
from math import *
###########################################################################
def hesab(l1,l2,tt1,tt2,yn1,yn2):
    ######################formula##########################
    x1=l1*cos(tt1)
    x2=l2*cos(tt1+tt2)
    y1=l1*sin(tt1)
    y2=l2*sin(tt1+tt2)
    xe=x1+x2
    ye=y1+y2
    #####################matplot###########################
    ylabel('mehvare Y')
    xlabel('mehvare X')
    title("moghtasad x,y: xe = "+str(xe)+"ye = "+str(ye))
    if(yn1 == 'yes'):
        grid(True)
    else:

        grid(False)
    if(yn2 == 'yes'):
        plot([0,x1,xe],[0,y1,ye])
        plot([0,x1,xe],[0,y1,ye],'ro')
    else:
        plot([0,x1,xe],[0,y1,ye])
    show()
    
###########################################################################
yn1 = input("aya nmudar be shekl jadaval bashad? javab ba : yes va no  ")
yn2 = input("aya joint ha moshakas shavad? : yes va no  ")
l1 = float(input("andaze ye bazo1  "))
l2 = float(input("andaze ye bazo2  "))
tt1 = radians(float(input("zavie 1  ")))
tt2 = radians(float(input("zavie 2  ")))
###########################################################################
hesab(l1,l2,tt1,tt2,yn1,yn2)
