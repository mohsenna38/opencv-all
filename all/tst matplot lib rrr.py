from matplotlib.pyplot import *
from math import *
from numpy import *
while True:
    yn1 = "yes"#input("aya nmudar be shekl jadaval bashad? javab ba : yes va no  ")
    yn2 = 'yes'#input("aya joint ha moshakas shavad? : yes va no  ")
    l1 = float(input("andaze yeye bazo1  "))
    l2 = float(input("andaze yeye bazo2  "))
    l3 = float(input("andaze yeye bazo3  "))
    tt1 = deg2rad(float(input("zavie 1  ")))
    tt2 = deg2rad(float(input("zavie 2  ")))
    tt3 = deg2rad(float(input("zavie 3  ")))

###########################################################################
    def hesab(l1,l2,l3,tt1,tt2,tt3,yn1,yn2):
        ######################formula##########################
        x1=l1*cos(tt1)
        x2=l2*cos(tt1+tt2)
        x3=l3*cos(tt1+tt2+tt3)
        y1=l1*sin(tt1)
        y2=l2*sin(tt1+tt2)
        y3=l3*sin(tt1+tt2+tt3)
        xe=x1+x2+x3
        ye=y1+y2+y3
    #####################matplot###########################
        ylabel('mehvare Y')
        xlabel('mehvare X')
        title("xe = "+str(xe)+"ye = "+str(ye))
        if(yn1 == 'yes'):
            grid(True)
        else:
            grid(False)
        if(yn2 == 'yes'):
            plot([0,x1,x1+x2,xe],[0,y1,y1+y2,ye])
            plot([0,x1,x1+x2,xe],[0,y1,y1+y2,ye],'ro')
        else:
            plot([0,x1,x2,xe],[0,y1,y2,ye])
        show()
    
###########################################################################
###########################################################################
    hesab(l1,l2,l3,tt1,tt2,tt3,yn1,yn2)
