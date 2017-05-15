
state = 0
inputarray =[
"6",
"0 0 0 0 1 0"
]

inputarray2 =[
"7",
"0 0 1 0 0 1 0"
]

def input():
    global state
    result = inputarray2[state]
    state += 1
    return result

import sys


#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
cnt = 0
i = 0
while i < n:
    if i < n-2  and c[i+2] == 0:
        i += 2
        cnt += 1
    elif i < n - 1 and c[i + 1] == 0:
        i += 1
        cnt += 1
    else:
        i += 1
        if i < n:
            cnt += 1
print(cnt)
