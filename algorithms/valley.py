#!/bin/python3
import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"8",
"UDDDUDUU"
]

def input():
    global state
    result = inputarray1[state]
    state += 1
    return result



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


