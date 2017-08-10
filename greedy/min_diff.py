#!/bin/python3



inputarray = [
"3",
"3 -7 0"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys



n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
sa = sorted(a)
mdf = None
for i, e in enumerate(sa[:-1]):
    dfs = abs(sa[i+1]-sa[i])
    mdf = dfs if mdf == None or dfs < mdf else mdf
print(mdf)