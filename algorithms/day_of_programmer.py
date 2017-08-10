#!/bin/python3
import sys


#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"2017"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray)


def is_leap(year):
    if (year > 1918):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    else:
        return (year % 4 == 0 )

month_days = [31,28,31,30,31,31,30,31,30,31,30,31]

def get_day(year):
    m = list(month_days)
    if (is_leap(year)):
        m[1] = 29
    if (year == 1918):
        m[1] -= 13
    start,count = 256,0
    while start > m[count]:
        start -= m[count]
        count += 1
    return (start, count+1, year)
import sys

def solve(year):
    return get_day(year)

year = int(input().strip())
result = solve(year)
print("{:0>2}.{:0>2}.{:0>4}".format(*result))
