#FIRST EVEN DIGIT AND DIGIT NEXT TO EVEN

n=int(input('Enter n:'))
rev=0
list=[]

while(n>0):
      rev=rev*10+n%10
      n=n//10
while(rev>0):
      r=rev%10
      d=[r]
      list=list+d
      rev=rev//10
print(list)
for i in list:
      if(i%2==0):
            print('First even digit:',i)
            k=i
            break
k=int(list.index(i))
print('The digit next to even:',list[k+1])
            
"""
number: 976487
first even digit is 6
digit next to even is 4
      
 


        
        
          
        
              
