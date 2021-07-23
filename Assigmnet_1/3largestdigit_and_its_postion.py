# THE BIGGEST DIGIT IN A NUMBER

""" THIS PROGRAM WORKS FOR ONLY NON REPEATED DIGITS. """

n=int(input('Enter the Number:'))
l=0
count=0


while(n>0):
    r=int(n%10)
    n=n//10
    count=count+1
    if(r>l):
        l=r
        j=int(count)
p=int(count-j+1)
print('The largest digit is:',l)
print('position',p)


"""
NUMBER : 45978
LARGEST DIGIT IS 9
POSITION IS 3
"""


    

