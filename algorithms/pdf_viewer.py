

inputarray =[
"1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5",
"abc"

]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
hm = {chr(ord('a')+i):l for i,l in enumerate(h)}
print(len(word)*hm[max(list(word),key=lambda x: hm[x])])

