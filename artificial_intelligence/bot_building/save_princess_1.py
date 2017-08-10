#!/usr/bin/python
import sys


inputarray = [
"3",
"---",
"-m-",
"p--"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)

def displayPathtoPrincess(n,grid):
    for gi, gy in enumerate(grid):
       if 'm' in gy:
           my,mx = gi,gy.index('m')
       if 'p' in gy:
           py,px = gi,gy.index('p')

    while my < py:
        print('DOWN')
        my += 1
    while my > py:
        print('UP')
        my -= 1
    while mx < px:
        print('RIGHT')
        mx += 1
    while mx > px:
        print('LEFT')
        mx -= 1


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
