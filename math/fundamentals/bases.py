#!/bin/python3

import sys
#!/bin/python3

import sys


inputarray = [
"2 2"
]




from tools import input, initArrayInputter
initArrayInputter(inputarray)

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
print( ((m+1)//2) *((n+1)//2) )