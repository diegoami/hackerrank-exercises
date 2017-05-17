#!/bin/python3

state = 0

inputarray = \
[
"haveaniceday",
]
inputarray2 = \
[
"feedthedog",
]

inputarray3 = \
[
"chillout",
]
def input():
    global state
    result = inputarray2[state]
    state += 1
    return result
#!/bin/python3



#!/bin/python3

import sys

import math
s = input().strip()
mini = math.ceil(math.sqrt(len(s)))
minj = math.ceil(math.sqrt(len(s)))

sa =[""]*minj

for i in range(mini):
    for j in range(minj):

        if (i*minj+j) < len(s):
            sa[j] = sa[j] +s[i*minj+j]
print(*sa,sep=' ')