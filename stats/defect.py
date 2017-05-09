state = 0
inputarray = ["1.09 1"]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys

F, S = map(float,input().split())


def binom(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        ln = binom(n-1)
        return [1] +[ (ln[i]+ln[i+1]) for i in (range(len(ln)-1))]+ [1]


bin = binom(7)

probm = F/(S+F)
probf = 1 - probm


probt =  bin[3]*(probm**3)*(probf**3) + bin[2]*(probm**4)*(probf**2) +  bin[1]*(probm**5)*(probf)+bin[0]*(probm**6)
print("{:.3}".format(probt))