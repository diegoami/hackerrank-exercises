
inputarray = [
"3",
"12",
"5",
"7"
]

inputarray2 = [
"1",
"1"

]


from tools import input, initArrayInputter
initArrayInputter(inputarray2)

import math
def prime(v):
    if (v < 2):
        return False
    for i in range(2,math.floor(math.sqrt(v)+1)):
        if v % i == 0:
            return False
    return True



n = int(input())
for i in range(n):
    c = int(input())
    print("Prime" if prime(c) else "Not prime")