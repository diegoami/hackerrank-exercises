#!/bin/python3
import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"9",
"10 20 20 10 10 30 50 10 20"
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import collections as col
import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
cnt = col.Counter(c)
matching = sum([cnt[x]//2 for x in cnt ])
print(matching)