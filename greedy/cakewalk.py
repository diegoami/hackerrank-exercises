state = 0

inputarray = [
"3",
"1 3 2"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
sclor = sorted(calories,reverse=True)
rst = 0
for i,e in enumerate(sclor):
    rst += e* 2**i

print(rst)