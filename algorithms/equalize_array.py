

inputarray =[
"5",
"3 3 2 1 3"
]




from tools import input, initArrayInputter
initArrayInputter(inputarray)


import sys
import collections

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split()]
cnter = collections.Counter(A)
frqn= cnter.most_common()[0][1]
print(len(A)-frqn)
print(len(A)-collections.Counter(A).most_common()[0][1])
