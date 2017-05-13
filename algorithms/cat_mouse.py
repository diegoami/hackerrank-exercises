#!/bin/python3
import sys

state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"3",
"1 2 3",
"1 3 2",
"2 1 3"
]
def input():
    global state
    result = inputarray1[state]
    state += 1
    return result

def whichcat(cA,cB,M):
    if abs(cA-M) < abs(cB-M):
        print("Cat A")
    elif abs(cA-M) > abs(cB-M):
        print("Cat B")
    else:
        print("Mouse C")

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    whichcat(x, y, z)
