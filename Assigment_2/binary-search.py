 #BINARY SEARCH

pos=0

def search(a,n): 
    l=0
    u=len(a)-1
    while l<=u:
        mid=(l+u)//2
        if a[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if a[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

a=[4,7,8,12,99,102,702,10987,56666]
n=100

if search(a,n):
    print('Found at',pos)
else:
    print('Not Found')

