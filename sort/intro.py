import sys


#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"4",
"6",
"1 4 5 7 9 12",
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys
V = int(input())
n = int(input())
l = list(map(int,input().split()))
print(l.index(V))