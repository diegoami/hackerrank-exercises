#!/bin/python3
import sys

state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray1 = [
"10",
"1 97",
"2",
"1 20",
"2",
"1 26",
"1 20",
"2",
"3",
"1 91",
"3"
]
def input2():
    global state
    result = inputarray1[state]
    state += 1
    return result


state = 1
import linecache
def input():
    global state
    result = linecache.getline('tc_8.txt', state)
    state += 1
    return result


from collections import deque
#dq = deque()
dq = []
dqs = []

removed = []
n = int(input())
crmx = None
for i in range(n):

    cmd = list(map(int,input().split()))

    if cmd[0] == 1:
        dq.append(cmd[1])
        if (crmx == None or cmd[1] > crmx):
            crmx = cmd[1]
    elif cmd[0] == 2:
        ppd = dq.pop()
        removed.append(ppd)
    elif cmd[0] == 3:
        if (crmx in removed):
            dqs = sorted(dq,reverse=True)
            crmx = dqs[0]
            removed = []
        print(crmx)




