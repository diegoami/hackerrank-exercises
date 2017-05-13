#!/bin/python3

import sys
state = 0


inputarray = [
"2",
"Hacker",
"Rank"
]


def input():
    global state
    result = inputarray[state]
    state += 1
    return result



import sys
import itertools

n = int(input())
strs = []
stroe = []
for i in range(n):
    s = input()
    strs.append(s)
    stre = s[1::2]
    stro = s[0::2]
    stroe.append(stro+" "+stre)
for s in stroe:
    print(s)