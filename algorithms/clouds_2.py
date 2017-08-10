

inputarray =[
"8 2",
"0 0 1 0 0 1 1 0"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
E = 100
for i in range(0,n,k):
    E -= 3 if c[i] == 1 else 1
print(E)



