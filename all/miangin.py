def arraymin(A):
    lenA = len(A)
    lenB = len(A[0])
    lenC = len(A[0][0])
    a = []
    b = []
    c = []
    d = []
    f = []
    ma = 0
    mb = 0
    mc = 0
    md = 0
    for n in range (0 ,lenA):
        for x in range(0,lenB):
            for z in range(0,lenC):
                    if(0 == z):
                        a = a + [A[n][x][z]]
                    if(1 == z):
                        b = b + [A[n][x][z]]
                    if(2 == z):
                        c = c + [A[n][x][z]]
                    if(3 == z):
                        d = d + [A[n][x][z]]
    print(a)
    print(b)
    print(c)
    print(d)
    lenD = len(a)
    for y in range(0,lenD):    
        ma = ma + a[y]
        mb = mb + b[y]
        mc = mc + c[y]
        md = md + d[y]
    f = f + [int(ma/lenD)] + [int(mb/lenD)] + [int(mc/lenD)] + [int(md/lenD)]
    print(ma)
    print(mb)
    print(mc)
    print(md)
    print(f)
    return f
