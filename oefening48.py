h1 = int (input()) 
w1 = int (input()) 

#Guessing first cell color
if ((h1 % 2 != 0) and (w1 % 2 != 0)) or ((h1 % 2 == 0) and (w1 % 2 == 0)):
    print('DONKER VELD')
else:
     print('LICHT VELD')
