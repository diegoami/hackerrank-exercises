#!/bin/python3

import sys



inputarray = [
"6",
"1 4 4 4 5 3"
]


from tools import input, initArrayInputter
initArrayInputter(inputarray)



#!/bin/python3

import sys
from collections import Counter


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
stypes = sorted(set(types), key=types.count, reverse=True)[0]
print(stypes)
birds = {}
mvs = 0
lf = []
for t in types:
    birds[t] = birds[t] + 1 if t in birds else 1
    if birds[t] > mvs:
        mvs = birds[t]
        lf = [t]
    elif birds[t] == mvs:
        lf.append(t)
print(min(lf))
birds = Counter(types)  # Counts the array into a dictionary
print(birds.most_common(1))