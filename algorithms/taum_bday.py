#!/bin/python3

import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = \
[
"5",
"10 10",
"1 1 1",
"5 9",
"2 3 4",
"3 6",
"9 1 1",
"7 7",
"4 2 1",
"3 3",
"1 9 2",
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]


    if (y >= x + z + 1) and (x >= y + z + 1):
        print(b*x+w*y)
    elif (y >= x + z + 1) :
        print(b * x + w * (z + x))
    elif (x >= y + z + 1):
        print(b * (z + y) + w * y)
    else:
        print(b * x + w * y)