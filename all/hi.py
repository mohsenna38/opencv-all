vorodi=input('yechi bugo')
ragham = len(vorodi)
vorodi=int(vorodi)
num = 0
for y in range(0,3):
 numrgh = vorodi%2
 num = numrgh*(10**(2-y))+num
 vorodi =int(vorodi / 2) 
 print(num)
