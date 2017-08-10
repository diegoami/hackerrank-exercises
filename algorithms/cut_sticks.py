

inputarray =[
    "6",
"5 4 4 2 2 8"
]


inputarray2 =[
"8",
"1 2 3 4 3 3 2 1"
]


from tools import input, initArrayInputter
initArrayInputter(inputarray2)

import sys


#!/bin/python3

import sys


#!/bin/python3

import sys



n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
cuts = []
while any([x>0 for x in arr]):
    posx = [x for x in arr if x > 0]
    cuts.append(len(posx))
    minx = min(posx)
    arr = [x-minx for x in arr]
print(*cuts, sep='\n')