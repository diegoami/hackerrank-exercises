#!/bin/python


inputarray = [
"13"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

n = int(input().strip())
c1 = ""
seq1, maxseq1 = 0, 0
for k in range(22, -1, -1):
    ev = 1 << k
    if n >= ev:
        c1 = c1 + "1"
        n -= ev
        seq1 += 1
        if seq1 > maxseq1:
            maxseq1 = seq1
    else:
        c1 = c1 + "0"
        seq1 = 0

print(maxseq1)
