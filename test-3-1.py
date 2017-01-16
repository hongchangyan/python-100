#!/usr/bin/python
# -*- coding:utf-8 -*-
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print fib(6).next()
#for i in fib(6):
#    print i
