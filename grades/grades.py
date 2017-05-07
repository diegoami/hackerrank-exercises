#!/bin/python3

import sys
def input():
    for i in [ "4", "73", "67", "38", "33"]:
        yield i



def process(grade):
    result = grade if ( grade < 38 or grade % 5 <= 2 ) else (int(grade / 5 ) +1) *5
    return str(result).strip()

def solve(grades):
    return map(process, grades)


result = solve([73, 67, 38, 33])
print (" ".join(map(str, result)))