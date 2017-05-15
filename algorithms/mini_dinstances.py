
state = 0
inputarray =[
"6",
"7 1 3 4 1 7",
]




def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys


#!/bin/python3

import sys


#!/bin/python3

import sys


#!/bin/python3

import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
minx = -1
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if (A[i] == A[j]):
            if minx == -1 or abs(i-j) < minx:
                minx = abs(i-j)
print(minx)