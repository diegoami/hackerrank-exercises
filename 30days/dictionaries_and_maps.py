
inputarray = [
"3",
"sam 99912222",
"tom 11122222",
"harry 12299933",
"sam",
"edward",
"harry"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)
dic = {}
import sys
n = int(input())
for i in range(n):
    k, v = input().split()
    dic[k] = v
while True:
    try:
        x = input()
        if (x):
            if x in dic:
                print("{}={}".format(x,dic[x]))
            else:
                print("Not found")
    except:
        break


