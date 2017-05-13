#!/bin/python3

import sys
state = 0


inputarray = [
"6 3",
"1 3 2 6 1 2"
]


def input():
    global state
    result = inputarray[state]
    state += 1
    return result



import sys
import itertools

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))

cx = itertools.combinations(a,2)
count = 0
for c in cx:
    if ((c[0]+c[1]) % k == 0):
        count += 1
print(count)


