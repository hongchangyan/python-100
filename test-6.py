#!/usr/bin/python

#def fib(n):
#    a,b = 1,1
#    for i in range(n-1):
#        a,b = b,a+b

#    return [a,b]
#
#print fib(10)

def fib(n):
    fibs = [1, 1]
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        for i in range(2,n):
            
            fibs.append(fibs[-1] +fibs[-2])
    return fibs

print fib(20)
