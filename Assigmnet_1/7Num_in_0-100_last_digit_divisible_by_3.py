#PRINT A NUMBER BETWEEN 0 TO 100 WHOSE LAST DIGIT IS DIVISIBLE BY 3

for i in range(0,100):
    r=int(i%3)
    if(r==0):
        print('The required number:',i)
