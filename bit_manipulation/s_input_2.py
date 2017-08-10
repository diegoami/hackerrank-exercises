#!/usr/bin/py
# Head ends here



inputarray = [
"5",
"0 0 1 2 1"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray)

def lonelyinteger(b):
    import functools as ft
    return ft.reduce(lambda x,y: x ^ y, b)

# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
