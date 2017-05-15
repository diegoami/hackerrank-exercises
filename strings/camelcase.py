#!/bin/python3

import sys
import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"saveChangesInTheEditor"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result

s = input().strip()
numU = len([x for i,x in enumerate(s) if i > 0 and x.isupper()])+1
print(numU)