#!/usr/bin/python
state = 0

inputarray = [
"0 0",
"b---d",
"-d--d",
"--dd-",
"--d--",
"----d"
]

inputarray2 = [
"0 0",
"b---d",
"----d",
"-----",
"-----",
"ddd--"
]

inputarray3 = [
"1 2",
"-----",
"--b--",
"-----",
"-----",
"ddd--"
]


def input():
    global state
    result = inputarray[state]
    state += 1
    return result

# Head ends here
def next_move(posr, posc, board):
    csdy, csdx = None,None
    for bi, by in enumerate(board):
        for bj, bx in enumerate(by):
            if bx == 'd':

                if (csdy, csdx) == (None, None):
                    csdy, csdx = bi, bj
                else:
                    if (abs(csdy-posr) +  abs(csdx-posc)) > (abs(bi-posr) +  abs(bj-posc)):
                        csdy, csdx = bi, bj
    if (csdy, csdx) == (posr, posc):
        return 'CLEAN'
    elif (csdy, csdx) == (None, None):
        return 'FINISHED'
    else:
        if posc < csdx:
            return 'RIGHT'
        elif posc > csdx:
            return 'LEFT'
        elif posr < csdy:
            return 'DOWN'
        elif posr > csdy:
            return 'UP'
        return 'FINISHED'
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    while True:
        board[pos[0]][pos[1]] = '-'
        moveDone = next_move(pos[0], pos[1], board)
        print (moveDone)
        if (moveDone == 'CLEAN'):
            board[pos[0]][pos[1]] = '-'
        elif (moveDone == 'LEFT'):
            pos[1] -= 1
        elif (moveDone == 'RIGHT'):
            pos[1] += 1
        elif (moveDone == 'UP'):
            pos[0] -= 1
        elif (moveDone == 'DOWN'):
            pos[0] += 1
        board[pos[0]][pos[1]] = 'b'
        for b in board:
            print(b)
        if (moveDone == 'FINISHED'):
            break
