#FIRST EVEN DIGIT AND ITS POSITION OF A NUMBER

n=int(input('Enter Number:'))
rev=0
count=0


while (n>0):
    rev=(rev*10)+n%10
    n=n//10
    
print(rev)
while(rev>0):
    d=int(rev%10)
    rev=rev//10
    count=count+1
    if(d%2==0):
        print('The first even digit is:',d)
    else:
        print('There is no even digit')
        
print('The position of even digit is:',count)            
    
