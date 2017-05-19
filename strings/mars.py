#!/bin/python3

import sys
import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"SOSSPSSQSSOR"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result



S = input().strip()
print(len(([(i,x)  for i, x in enumerate(S) if (i % 3 in [2,0] and x != 'S') or (i % 3 ==1  and x != 'O')])))

#ll = len([1 for i, x in enumerate(S) if (i % 3 in [1,0] and x != 'S')])+len([1 for i, x in enumerate(S) if (i % 3 == 2 and x != '0')])
#print(ll)