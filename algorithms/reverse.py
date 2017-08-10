#!/bin/python3

import sys

inputarray = ["1 1 1 0 0 0",""]
def input():
    global state
    if (state == 0):
        result = "4"
    else:
        result = "1 4 3 2"
    state  += 1
    return result

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.reverse()
print(" ".join(map(str, arr)))