#!/bin/python

state = 0
inputarray = [
"aba",
"10"
]

inputarray2 = [
"6",
"4 6 5 3 3 1"
]


def input():
    global state
    result = inputarray[state]
    state += 1
    return result

#!/bin/python3

import sys


#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())

na = s.count('a')
if (n % len(s) == 0 ):
    v = int(na * (n / len(s)))
    print(v)
else:
    v = na * ( n // len(s))
    v += s[:n % len(s)].count('a')
    print(v)