#THE NUMBER IS PALLINDROME OR NOT

num=int(input('Enter the number:'))
x=num
rev=0
while(num>0):
    rev=(rev*10)+num%10
    num=num//10
if(x==rev):
        print('The number is pallindrome')
else:
        print('The number is not pallindrome')
        
