#!/usr/bin/python
# -*- coding: utf-8 -*-

i = int(raw_input('please input your pofit:'))

arr = [1000,500,100,0]
rat = [0.1,0.2,0.3,0.4]
r = 0

for idx in range(0,4):
	if i>arr[idx]:
		print idx
		r+=(i-arr[idx])*rat[idx]
		print (i-arr[idx])*rat[idx]
		
		i=arr[idx]
print r		
