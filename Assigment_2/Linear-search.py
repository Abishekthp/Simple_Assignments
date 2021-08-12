#LINEAR SEARCH

pos=-1 #(global variable)

def search(a,n):
    i=0
    while i<len(a):
        if a[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
    
a=[5,8,4,6,9,2]
n=9

if search(a,n):
    print('found at',pos)
else:
    print('Not Found')
