#!/usr/bin/py
# Head ends here



inputarray = [
"3 ",
"2147483647",
"1 ",
"0"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray)


# Tail starts here
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x = int(input())
        bx = bin(x)[2:].zfill(32)
        #print(bx)
        bfl = ''.join(['1' if bx[i] == '0' else '0' for i in range(len(bx))])
        print(int(bfl, 2))

