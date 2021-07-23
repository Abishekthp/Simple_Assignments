#PRINT NUMBERS BETWEEN 20 TO 70 EITHER MULTIPLES OF 3 OR 7 AND FIND SUM

sum=0
print('THE REQUIRED NUMBERS:')
for i in range(20,70+1):
    if(i%3==0 or i%7==0):
        
            print(i)
            sum=sum+i
print('sum:',sum)
