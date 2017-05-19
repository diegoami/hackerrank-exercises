#!/bin/python3

import sys
import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"We promptly judged antique ivory buckles for the next prize"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result




S = input().strip()
print("pangram" if set([x.lower() for x in S if x.isalpha()] ) == set('abcdefghijklmnopqrstuwvxywz') else "not pangram")
