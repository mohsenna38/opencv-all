def arraymin(A):
    lenA = len(A)
    lenB = len(A[0])
    lenC = 3
    a = []
    b = []
    c = []
    d = []
    ma = 0
    mb = 0
    mc = 0
    for n in range (0 ,lenA):
        for x in range(0,lenB):
            for z in range(0,lenC):
                    if(0 == z):
                        a = a + [A[n][x][z]]
                    if(1 == z):
                        b = b + [A[n][x][z]]
                    if(2 == z):
                        c = c + [A[n][x][z]]
    print(a)
    print(b)
    print(c)
    
    lenD = len(a)
    for y in range(0,lenD):    
        ma = ma + a[y]
        mb = mb + b[y]
        mc = mc + c[y]
    d = d + [int(ma/lenD)] + [int(mb/lenD)] + [int(mc/lenD)]
    print(ma)
    print(mb)
    print(mc)
    print(d)
    return d
