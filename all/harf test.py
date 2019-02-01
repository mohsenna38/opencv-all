from time import *
times = perf_counter()
with open ("HW.txt",'r') as matn:
    harfa = matn.read()
##########################################################
def yabande(file,letter):
    shomar = 0
    for hrf in file:
        if letter == hrf:
            shomar = shomar + 1   
    return shomar
##########################################################
yabande(harfa,'G')
print(perf_counter() - times)

