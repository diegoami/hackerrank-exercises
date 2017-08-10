

inputarray = [
"3",
"1 3 2"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
sclor = sorted(calories,reverse=True)
rst = 0
for i,e in enumerate(sclor):
    rst += e* 2**i

print(rst)