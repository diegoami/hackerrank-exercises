state = 0

inputarray = [
"3",
"2 3 1"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys


n = int(input().strip())
s = list(map(int,input().split()))
p, q = {}, {}
for i,e in enumerate(s):
    p[i+1]=e
    q[e] = i+1
for x in range(1,n+1):
    print(q[q[x]])


