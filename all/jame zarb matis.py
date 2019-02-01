from time import *
timestart = perf_counter()
d = 0
for a in range(1,10):
    for b in range(1,10):
        c = a*b
        d = d + c
        print(c,'',end='')
    print('')
print(timestart,d)
