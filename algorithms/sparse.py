#!/bin/python3

import sys


#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"4",
"aba",
"baba",
"aba",
"xzxb",
"3",
"aba",
"xzxb",
"ab",
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

x = arr
max_c = None
for i in range(1,len(x)-1):
    for j in range(1,len(x[i])-1):
        c = x[i][j]+x[i-1][j]+x[i+1][j]+x[i-1][j-1]+x[i+1][j-1]+x[i-1][j+1]+x[i+1][j+1]
        max_c = c if (max_c == None or c > max_c) else max_c


print(max_c)