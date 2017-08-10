#!/bin/python3

import sys



inputarray = [
"2",
"Hacker",
"Rank"
]


from tools import input, initArrayInputter
initArrayInputter(inputarray)



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