#!/bin/python3



inputarray1 = [
"10 2 3",
"3 1",
"5 2 8"
]
inputarray2 = [
"5 1 1",
"4",
"5"
]


from tools import input, initArrayInputter
initArrayInputter(inputarray2)

import sys
import itertools as it

def getMoneySpent(keyboards, drives, s):
    kdp = list(it.product(keyboards,drives))
    kdf = list(it.filterfalse(lambda x: x[0]+x[1] > s, kdp ))
    return sum(max(kdf,key=lambda x: x[0]+x[1])) if len(kdf) > 0 else -1

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of target_money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
