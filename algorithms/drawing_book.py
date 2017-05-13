#!/bin/python3
import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"6",
"2"
]
inputarray2 = [
"5",
"4"
]
def input():
    global state
    result = inputarray1[state]
    state += 1
    return result

def solve(n, p):
    n = n if n % 2 == 0 else n-1
    p = p if p % 2 == 0 else p-1
    df = (p)//2
    de = (n-p)//2
    return min(df,de)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)