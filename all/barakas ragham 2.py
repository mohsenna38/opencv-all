vorodi=input('yechi bugo')
ragham = len(vorodi)
vorodi=int(vorodi)
num = 0
for y in range(ragham,0,-1):
 numrgh = vorodi%10
 num = numrgh*(10**(y-1))+num
 vorodi =int(vorodi / 10) 
 print(num)
