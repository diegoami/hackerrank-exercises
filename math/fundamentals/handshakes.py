#!/bin/python3

import sys

state = 0

inputarray = [
"2",
"1",
"2"
]

# 2 --> 1
# 3 --> 3
# 4 --> 6
# 5 --> 10


def input():
    global state
    result = inputarray[state]
    state += 1
    return result

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    print(int(N*(N-1)/2))
