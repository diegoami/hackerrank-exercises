import sys
state = 0
inputarray = [
"2",
"2",
"1 1",
"3",
"2 1 4",
]

def input():
    global state
    if (state < len(inputarray)):
        result = inputarray[state]
        state += 1
        return result
    else:
        return None

import functools

def xor(a,b):
    return a ^ b

def xorlist(l):
    return functools.reduce(xor, l)

NG = int(input())
games = []
for i in range(NG):
    game = {}
    game["npiles"] = int(input())
    game["piles"] =  list(map(int,input().split()))
    game["wins"]  =  "Second" if xorlist(game["piles"]) == 0 else "First"
    games.append(game)

for g in games:
    print(g["wins"])