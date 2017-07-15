#!/bin/python3

import sys
#!/bin/python3

import sys
state = 0

inputarray = [
"2 2"
]




def input():
    global state
    result = inputarray[state]
    state += 1
    return result

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
print( ((m+1)//2) *((n+1)//2) )