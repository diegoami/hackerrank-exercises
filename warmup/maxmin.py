#!/bin/python3

import sys


#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"6",
"3",
"10",
"20",
"30",
"100",
"101",
"102",
]


inputarray1 = [
"10",
"4",
"1",
"2",
"3",
"4",
"10",
"20",
"30",
"40",
"100",
"200",
]        



from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys
arr = []
N = int(input())
K = int(input())
for i in range(N):
   arr.append(int(input()))

sarr = sorted (arr)
cm = None
for i in range(0,N-K+1):
    slist = sarr[i:i+K]
    print(slist)
    mdiff = (max(slist)-min(slist))
    cm = cm if (cm and cm < mdiff) else (mdiff)
print(cm)

#cit= itertools.combinations(arr,K)
#max_cit = min(cit, key= lambda c: max(c)-min(c) )
