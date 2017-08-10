#!/bin/python3

import sys



inputarray = [
"2",
"1",
"2"
]

# 2 --> 1
# 3 --> 3
# 4 --> 6
# 5 --> 10


from tools import input, initArrayInputter
initArrayInputter(inputarray)

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    print(int(N*(N-1)/2))
