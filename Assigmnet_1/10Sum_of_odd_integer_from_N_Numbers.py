#READ N & N NUMBERS AND FIND THE SUM OF ODD INTEGERS

n=int(input('Enter n:'))
sum=0

for i in range(0,n):
    N=int(input('Give N:'))
    if(N%2!=0):
        sum=sum+N
    
print('Sum of Odd numbers:',sum)

"""
GIVE 4 NUMBERS.
NUMERS ARE 233,234,255,257
SUM WILL BE 233+234+255=745
"""
