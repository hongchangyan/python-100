#!/usr/bin/python

year = int(raw_input('please input year:'))
month = int(raw_input('please input month:'))
day = int(raw_input('please input day:'))

days = (0,31,59,90,120,151,181,212,243,273,304,334)
pre_month_days = 0

if (0 < month < 12) and (0 < day < 31):
    for i in range(1, month+1):
        print i
        if i in [1,3,5,7,8,10,12]:
            pre_month_days += 31
        elif i == 2:
            pre_month_days += 28
        else:
            pre_month_days +=30
        print pre_month_days
else:
    print 'data error ,please check day or month'
    exit()
days = pre_month_days + day
flag = 0

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    flag = 1

if (flag == 1) and (month > 2):
    days += 1

print 'it is the %s days' % days
