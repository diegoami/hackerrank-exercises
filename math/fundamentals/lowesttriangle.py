#!/bin/python3

import sys
state = 0

inputarray = [
"17 100"
]


def input():
    global state
    result = inputarray[state]
    state += 1
    return result

def lowestTriangle(base, area):
    import math
    return math.ceil(area*2/base)


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
