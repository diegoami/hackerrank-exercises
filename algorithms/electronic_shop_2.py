#!/bin/python3
state = 0


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


def input():
    global state
    result = inputarray1[state]
    state += 1
    return result

import sys
import itertools as it

def getMoneySpent(keyboards, drives, s):
    comb=list(i+j for i in keyboards for j in drives if i+j <= s)
    return s - min(list(s-i for i in comb if i<=s)) if len(comb) > 0 else -1


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of target_money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
