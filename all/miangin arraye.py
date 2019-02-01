A = [100,200,200]
B = [140,250,100]
lenA = len(A)
lenB = len(B)
c = []
for z in range(0,lenA):
    for y in range(0,lenB):
        if(y == z):
            c = c + [(B[y]+A[z])/2]
            print(c)

