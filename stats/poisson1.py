state = 0
inputarray = [
    "2.5",
    "5"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys
import math
la = float(input())
k = float(input())
p = la**k*math.exp(-la)/math.factorial(k)
print(round(p,3))