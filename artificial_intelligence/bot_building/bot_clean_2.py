#!/usr/bin/python
state = 0

inputarray = [
"0 0",
"5 5",
"b---d",
"-d--d",
"--dd-",
"--d--",
"----d"
]


def input():
    global state
    result = inputarray[state]
    state += 1
    return result

# Head ends here
def next_move_sub(posy, posx, dimy, dimx, board):
    csdy, csdx = None, None
    for bi, by in enumerate(board):
        for bj, bx in enumerate(by):
            if bx == 'd':

                if (csdy, csdx) == (None, None):
                    csdy, csdx = bi, bj
                else:
                    if (abs(csdy - posy) + abs(csdx - posx)) > (abs(bi - posy) + abs(bj - posx)):
                        csdy, csdx = bi, bj
    if (csdy, csdx) == (posy, posx):
        print('CLEAN')
    #elif (csdy, csdx) == (None, None):
     #   return 'FINISHED'
    else:
        if posx < csdx:
            print('RIGHT')
        elif posx > csdx:
            print('LEFT')
        elif posy < csdy:
            print('DOWN')
        elif posy > csdy:
            print('UP')
        #return 'FINISHED'


def next_move(posy, posx, dimy, dimx, board):
    csdy, csdx = None,None
    for bi, by in enumerate(board):
        for bj, bx in enumerate(by):
            if bx == 'd':

                if (csdy, csdx) == (None, None):
                    csdy, csdx = bi, bj
                else:
                    if (abs(csdy-posy) +  abs(csdx-posx)) > (abs(bi-posy) +  abs(bj-posx)):
                        csdy, csdx = bi, bj
    if (csdy, csdx) == (posy, posx):
        return 'CLEAN'
    elif (csdy, csdx) == (None, None):
        return 'FINISHED'
    else:
        if posx < csdx:
            return 'RIGHT'
        elif posx > csdx:
            return 'LEFT'
        elif posy < csdy:
            return 'DOWN'
        elif posy > csdy:
            return 'UP'
        return 'FINISHED'
# Tail starts here
if __name__ == "__main__":

    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)

    while True:
        board[pos[0]][pos[1]] = '-'
        moveDone = next_move(pos[0], pos[1], dim[0], dim[1],  board)
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
