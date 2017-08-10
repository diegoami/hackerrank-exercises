

inputarray = [
"7 50",
"1 12 5 111 200 1000 10"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys


n,money = map(int,input().split())
toys = list(map(int, input().strip().split(' ')))
stoys  = sorted(toys)
cnt,idx = 0,0
while money > 0:
    money -= stoys[idx]
    if (money >= 0):
        cnt += 1
        idx += 1


print(cnt)