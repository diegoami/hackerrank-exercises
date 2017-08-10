
inputarray = [
    "1 3",
    "5"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

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
B=binom(I+1)
#print(B)
#print(P,I)
PL = [P*((1-P)**(I-1))*B[1], (P**2) *( (1-P)**(I-2))*B[2], (P**3) * ((1-P)**(I-3))*B[3] , (P**4) * ((1-P)**(I-4))*B[4] ,   (P**5) * ((1-P)**(I-5))*B[5]]
print(PL, sum(PL))
#PT = P*((1-P)**(I-1))+ P**2 * (1-P)**(I-2)*B[1] + P**3 * (1-P)**(I-3)*B[2] + P**4 * (1-P)**(I-4)*B[3] + P**5 * (1-P)**(I-5)*B[4]

print(round(sum(PL),3))