
inputarray = [
    "2.5",
    "5"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys
import math
la = float(input())
k = float(input())
p = la**k*math.exp(-la)/math.factorial(k)
print(round(p,3))