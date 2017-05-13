#!/bin/python3
import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"4 1",
"3 10 2 8",
"12"
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result


import sys


n,k = map(int,input().split())
c = list(map(int,input().split()))
pd = int(input())
tp = (sum(c)-c[k])/2
if (tp == pd):
    print("Bon Appetit")
else:
    print(int(pd-tp))