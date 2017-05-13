#!/bin/python3

import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"7 11",
"5 15",
"3 2",
"-2 2 1",
"5 -6"
]        



def input():
    global state
    result = inputarray[state]
    state += 1
    return result


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
print(len([x for x in apple if s <= x+a <= t ]), len([y for y in orange if s <= y+b <= t ]),sep = '\n')
