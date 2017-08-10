#!/bin/python3




inputarray1 = [
"9",
"10 5 20 20 4 5 2 25 1"
]

inputarray2 = [
"10",
"3 4 21 36 10 28 35 5 24 42"
]


def input():
    global state
    result = inputarray2    [state]
    state += 1
    return result

import sys

def getRecord(s):
    b,w = (None, None)
    nb, nw =0,0
    for i,l in enumerate(s):
        if (b,w) == (None,None):
            b,w  = l,l
        elif l > b :
            b = l
            nb += 1
        elif l < w:
            w = l
            nw += 1

    return (nb, nw)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))



