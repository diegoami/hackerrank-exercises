
inputarray = [
"9 6 2015",
"6 6 2015"
]
inputarray2 = [
"31 8 2004",
"20 1 2004"
]

inputarray3 = [
"2 6 2014",
"5 7 2014"
]
inputarray4 = [
"31 12 2009",
"1 1 2010"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray4)

import sys

d1,m1,y1 = map(int,input().split())
d2,m2,y2 = map(int,input().split())



def is_leap(year):
    if (year > 1918):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    else:
        return (year % 4 == 0 )

month_days = [31,28,31,30,31,31,30,31,30,31,30,31]

def get_day_years(yx):
    return 366 if is_leap(yx) else 365

def get_day_of_year(dx,mx,yx):
    m = list(month_days)
    if (is_leap(yx)):
        m[1] = 29
    if (yx== 1918):
        m[1] -= 13
    tot =  sum([m[i] for i in range(mx-1)])+dx

dp = 0
"""
if (y1 == y2):
    dp = get_day_of_year(d1,m1,y1)-get_day_of_year(d2,m2,y2)
elif (y1 == y2 + 1):
    dp = get_day_of_year(d1, m1, y1) + ( get_day_years( y2) - get_day_of_year(d2, m2, y2))
elif (y1 > y2):
    dp = get_day_of_year(d1, m1, y1) + ( get_day_years(y2) - get_day_of_year(d2, m2, y2))  + sum([get_day_years(y) for y in range(y1+1,y2-1)])
else:
    pass
print(dp*15)

"""

if (y1 > y2):
    dp = 10000
elif (y1 == y2) and (m1 > m2):
    dp = (m1-m2)*500
elif (y1 == y2) and (m1 == m2) and (d1 > d2):
    dp = (d1-d2)*15
else:
    pass
print(dp)