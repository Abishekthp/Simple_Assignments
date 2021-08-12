#FIBONACCI SEQUENCE TO PRINT THE NUMBBERS LESS THAN 100



def fib(n):
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        if(c<=100):
            print(c)
fib(100)
