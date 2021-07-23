#FIND THE FACTORS OF A NUMBER AND PRINT THE LARGEST FACTOR

n=int(input('Enter the number:'))
l=0

print('Factors are:')
for i in range(1,n):
    if(n%i==0):
        print(i)
        if(i>l):
            l=i
print('largest factor:',l)
