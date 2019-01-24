def map( x, in_min,in_max, out_min, out_max):
    maps = -((x - in_max)*(out_max-out_min)/(in_max-in_min)+out_min)
    print(maps)
    return maps
    
a = 0
b = 320
for j in range(a,b):
    map(j,b,a,0,1)
    