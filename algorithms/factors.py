#!/bin/python3

import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"2 3",
"2 4",
"16 32 96",
]        


inputarray = [
"2 3",
"3 9",
"81 232 424",
]
inputarray2 = [
"10 10",
"100 99 98 97 96 95 94 93 92 91",
"1 2 3 4 5 6 7 8 9 10"
]

inputarray3 = [

"1 3",
"2",
"20 30 12"
]

def input():
    global state
    result = inputarray1[state]
    state += 1
    return result


#!/bin/python3
import functools
aN, bN = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = sorted([int(arr_temp) for arr_temp in input().strip().split(' ')])
b = sorted([int(arr_temp) for arr_temp in input().strip().split(' ')])

#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))
# write your code here
