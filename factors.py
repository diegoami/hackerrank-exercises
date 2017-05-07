#!/bin/python3

import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"2 3",
"2 4",
"16 32 96",
]        


inputarray = [
"2 3",
"3 9",
"81 232 424",
]
inputarray2 = [
"10 10",
"100 99 98 97 96 95 94 93 92 91",
"1 2 3 4 5 6 7 8 9 10"
]

inputarray3 = [

"1 3",
"2",
"20 30 12"
]

def input():
    global state
    result = inputarray1[state]
    state += 1
    return result


#!/bin/python3
import functools
aN, bN = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = sorted([int(arr_temp) for arr_temp in input().strip().split(' ')])
b = sorted([int(arr_temp) for arr_temp in input().strip().split(' ')])

def gcd(a,b):
    while True:
        if (a == b):
            return a
        if (b > a):
            b -= a
        else:
            a -= b

def gcdl(l):
    sl = list(l)
    while True:
        if 0 in sl:
            sl.remove(0)
        if (len(sl) == 1):
            return sl[0]
        if (len(sl) == 2):
            return gcd(sl[0],sl[1])
        sl = sorted(sl)
        sl[-1] -= sl[-2]

def lcm(x,y):
    tmp=x
    while (tmp%y)!=0:
        tmp+=x
    return tmp

def lcml(*args):
    return functools.reduce(lcm,args)

al = lcml(*(a))
bg = gcdl(b)
al_o = al
count = 0
while al <= bg:
    if(bg % al) == 0:
        count += 1
    al = al + al_o

print(count)
