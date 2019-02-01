vorodi=input('yechi bugo')
ragham = len(vorodi)
vorodi=int(vorodi)
num = 0
for y in range(0,ragham):
 numrgh = vorodi%2
 num = numrgh*(10**(ragham-1-y))+num
 vorodi =int(vorodi / 10) 
 print(num)
