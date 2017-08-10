#!/bin/python3
import sys


#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"8",
"UDDDUDUU"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray1)



n = int(input())
ss = str(input())

lvl = 0
crs = 0
for s in ss:
    if s == 'D':
        lvl -= 1
    elif s == 'U':
        if lvl == -1:
            crs += 1
        lvl += 1
print(crs)


