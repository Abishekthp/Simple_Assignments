#PRINT THE NUMBERS BETWEEN 20 TO 70 EVEN & NOT MULTIPLES OF 3 AND 5

for i in range(20,70+1):
    if(i%2==0):
        if(i%3!=0):
            if(i%5!=0):

                print('The required number:',i)
