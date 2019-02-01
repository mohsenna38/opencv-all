from time import *
timestart = perf_counter()
a1 = int(input("add aval"))
a2 = int(input("add dovom"))
for a in range(1,a1+1):
    for b in range(1,a2+1):
        print(a*b,'',end='')
    print('')
print(timestart)
