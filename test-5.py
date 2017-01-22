#!/usr/bin/python

l = []

for i in range(1,4):
    x = int(raw_input('please input the %s number:' % i))
    l.append(x)

l.sort()

print l
