#!/bin/python3


state = 0

inputarray1 = [
"5",
"1 2 1 3 2",
"3 2",
]

inputarray2 = [
"6",
"1 1 1 1 1 1",
"3 2",
]

inputarray3 = [
"1",
"4",
"4 1",
]

def input():
    global state
    result = inputarray3[state]
    state += 1
    return result

import sys

import sys

def getWays(squares, d, m):
    w = 0
    for i, s in enumerate(squares):
        if sum(squares[i:i+m] ) == d:
            w +=1

    return w

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)




