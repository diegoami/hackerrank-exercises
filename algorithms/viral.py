#!/bin/python3
import sys




inputarray = [
"3"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray)



n = int(input())
tot = 0
liked = 2
for i in range(n):
    tot += liked
    liked = liked * 3 // 2
print(tot)


