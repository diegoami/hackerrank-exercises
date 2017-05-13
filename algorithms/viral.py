#!/bin/python3
import sys

state = 0


inputarray = [
"3"
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result



n = int(input())
tot = 0
liked = 2
for i in range(n):
    tot += liked
    liked = liked * 3 // 2
print(tot)


