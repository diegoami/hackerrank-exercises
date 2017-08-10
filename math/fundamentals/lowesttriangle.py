#!/bin/python3

import sys


inputarray = [
"17 100"
]


from tools import input, initArrayInputter
initArrayInputter(inputarray)

def lowestTriangle(base, area):
    import math
    return math.ceil(area*2/base)


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
