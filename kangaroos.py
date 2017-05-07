#!/bin/python3

import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"0 3 4 2"
]        

inputarray2= [
"0 2 5 3"
]


def input():
    global state
    result = inputarray1[state]
    state += 1
    return result


#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
"""
c = 0
while True:
    if ((x1 > x2) and (v1 > v2)) or ((x2 > x1) and (v2 > v1)):
        print("NO")
        break
    elif (x1 == x2):
        print("YES")
        break
    else:
        x1 += v1
        x2 += v2
        c += 1

"""
import math
if (x1 == x2):
    print("YES")
elif (v2 > v1):
    print("NO")
elif (v2 == v1):
    print("NO")
else:
    steps = (x2-x1)/(v1-v2)
    print("YES") if steps == math.floor(steps) else print("NO")