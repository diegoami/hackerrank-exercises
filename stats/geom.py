state = 0
inputarray = [
    "1 3",
    "5"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys
N, D = map(int,input().split())
I = int(input())

def binom(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        ln = binom(n-1)
        return [1] +[ (ln[i]+ln[i+1]) for i in (range(len(ln)-1))]+ [1]


P = N/D
print(P,I)
PT = P*((1-P)**(I-1))
print("{:.2}".format(PT))