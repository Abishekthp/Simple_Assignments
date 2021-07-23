#PRINT Y SUCH THAT DIGITS IN X WHICH ARE LESS THAN 5 ARE DOUBLED IN Y

n=int(input('Enter number:'))
rev=0
new=0

while(n>0):
    rev=(rev*10)+n%10
    n=n//10
print('Reverse is:',rev)
while(rev>0):
    r=int(rev%10)
    rev=rev//10
    if(r<5):
        r=2*r
    new=new*10+r
print('New number is:',new)
    
"""
Enter number 492784356.
New number will be 894788656
"""
