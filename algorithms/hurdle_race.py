#!/bin/python3
import sys




inputarray1 = [
"5 4",
"1 6 3 5 2"
]
inputarray2 = [
"5 7",
"2 5 4 5 2"
]

inputarray3 = [
"5 3",
"2 5 6 2 6"
]

inputarray4 = [
"5 1",
"2 5 6 2 6"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray4)



n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))



print(max(0,max(height)-k))