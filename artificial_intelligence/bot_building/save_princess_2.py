#!/usr/bin/python
import sys
state = 0

inputarray = [
"5",
"2 3",
"-----",
"-----",
"p--m-",
"-----",
"-----",
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result


def nextMove(n,r,c,grid):
    for gi, gy in enumerate(grid):
        if 'm' in gy:
            my, mx = gi, gy.index('m')
        if 'p' in gy:
            py, px = gi, gy.index('p')

    if r < py:
        return 'DOWN'

    if r > py:
        return 'UP'

    if c < px:
        return 'RIGHT'

    if c > px:
        return 'LEFT'


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
