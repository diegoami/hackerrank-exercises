state = 0
inputarray = ["12 10"]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys



def binom(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        ln = binom(n-1)
        return [1] +[ (ln[i]+ln[i+1]) for i in (range(len(ln)-1))]+ [1]




PC, B = map(float,input().split())
P = PC/100
bin = binom(B+1)
probm = bin[0]*((1-P)**B)+bin[1]*((1-P)**(B-1))*P+bin[2]*((1-P)**(B-2))*P**2
prob2 = 1-(bin[0]*((1-P)**B)+bin[1]*((1-P)**(B-1))*P)

print("{:.3f}".format(probm))
print("{:.3f}".format(prob2))