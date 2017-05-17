#!/bin/python

state = 0
inputarray = [
"6",
"1 2 2 3 1 2"
]

inputarray2 = [
"6",
"4 6 5 3 3 1"
]


def input():
    global state
    result = inputarray[state]
    state += 1
    return result



n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
l = sorted(a)
idx_m_1, m_idx, c_idx = 0, 0, 0

for i,e in enumerate(l):
    if i > 0 and e > l[idx_m_1]+1:
        idx_m_1 = i
        c_idx = 1
    else:
        c_idx += 1
    if c_idx > m_idx:
        m_idx = c_idx

print(m_idx)
