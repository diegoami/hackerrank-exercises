#!/usr/bin/py
# Head ends here
state = 0


inputarray = [
"5",
"0 0 1 2 1"
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result

def lonelyinteger(b):
    import functools as ft
    return ft.reduce(lambda x,y: x ^ y, b)

# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
