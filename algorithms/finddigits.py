
state = 0
inputarray =[
"2",
"12",
"1012"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n, c = int(input().strip()), 0
    for s in str(n):
        c += 1 if int(s) and n % int(s) == 0 else 0
    print(c)