#!/bin/python3

state = 0

inputarray = [
"3",
"3 -7 0"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys



n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
sa = sorted(a)
mdf = None
for i, e in enumerate(sa[:-1]):
    dfs = abs(sa[i+1]-sa[i])
    mdf = dfs if mdf == None or dfs < mdf else mdf
print(mdf)