state = 0
inputarray = [
    "0.88 1.55"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys
import math

def poisson(la,k):
    return la ** k * math.exp(-la) / math.factorial(k)

la1, la2 = map(float,input().split())
p1, p2 = poisson(la1,1), poisson(la2,1)
mla1, mla2 = la1+la1**2, la2+la2**2
c1, c2  = 160 + 40 * mla1, 128 + 40 * mla2
print(round(c1,3))
print(round(c2,3))