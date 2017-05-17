#!/bin/python

state = 0
inputarray = [
"13"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

n = int(input().strip())

seq1, maxseq1 = 0, 0
for k in range(22, -1, -1):
    ev = 1 << k
    if n & ev:

        seq1 += 1
        if seq1 > maxseq1:
            maxseq1 = seq1
    else:

        seq1 = 0

print(maxseq1)
