
state = 0
inputarray =[
"8 5",
"2 3 1 2 3 2 3 3",
"0 3",
"4 6",
"6 7",
"3 5",
"0 7",
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


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    print(min(width[i:j+1]))