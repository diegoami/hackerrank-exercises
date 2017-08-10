
inputarray = [
"10",
"10 0",
"0 10",
"-1 4",
"2 -3",
"-2 -2",
"5 6",
"3 3",
"8 0",
"2 3",
"3 -3"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)


import math
class Calculator:
    def power(self,n,p):
        if n >= 0 and p >= 0:
            return int(n**p)
        else:
            raise(Exception("n and p should be non-negative"))

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)