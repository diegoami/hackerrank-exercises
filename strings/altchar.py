#!/bin/python3

import sys
import sys


#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"5",
"AAAA",
"BBBBB",
"ABABABAB",
"BABABA",
"AAABBB"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)

n = int(input().strip())
for i in range(n):
    r = input().strip()
    cnt = 0
    sx = 0
    while True:
        idx1, idx2  =  r.find('AA',sx), r.find('BB',sx)
        if (idx1 == -1 and idx2 == -1):
            break
        else:
            cnt += 1
            sx = (idx1 if idx2 == -1 else idx2 if idx1 == -1 else min(idx1,idx2))+1

    print(cnt)
