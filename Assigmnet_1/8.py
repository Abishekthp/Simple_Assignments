#READ N AND N NUMBERS AND DELETE LAST SECOND DIGIT OF N NUMBERS AND FIND IT'S SUM

n=int(input('Enter n:'))
sum=0
for i in range(0,n):
    N=int(input('Give the value of number:'))
    r=N%100
    f=N//100
    d=r%10
    new=int(f*10+d)
    sum=sum+new
print('Sum:',sum)
        
"""
  Give 4 numbers.
  Numbers are 457,872,531,947.
  Output will be 47+82+51+97 = 277
"""
