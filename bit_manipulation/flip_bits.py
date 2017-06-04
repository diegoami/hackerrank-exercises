#!/usr/bin/py
# Head ends here
state = 0


inputarray = [
"3 ",
"2147483647",
"1 ",
"0"
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result


# Tail starts here
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x = int(input())
        bx = bin(x)[2:].zfill(32)
        #print(bx)
        bfl = ''.join(['1' if bx[i] == '0' else '0' for i in range(len(bx))])
        print(int(bfl, 2))

