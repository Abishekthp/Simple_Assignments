#READ N AND N NUMBERS AND FIND THE SUM OF LAST SECOND DIGIT OF N NUMBERS

n=int(input('Enter n:'))
sum=0

for i in range(0,n):
    N=int(input('Give n numbers:'))
    r=N%100
    f=int(r//10)
    sum=sum+f
    print('last second digit:',f)
print('sum:',sum)
