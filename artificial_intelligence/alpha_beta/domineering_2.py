from tools import input, initFileInputter
initFileInputter('dom_7.txt')

from copy import deepcopy
from random import  randint
import sys
import math


def revert(pch):
    if (pch == 'v'):
        return 'h'
    elif (pch == 'h'):
        return 'v'
    else:
        print("INCORRECT COLOR : {}".format(pch), file=sys.stderr)
        return pch

class Position:

    lx,ly = 8,8
    def __init__(self, input=None, board=None, pch=None):
        if (input):
            self.pch = input()
            self.board = []
            for _ in range(self.ly):
                carr = []
                self.board.append(carr)
                cl = input()
                for c in cl:
                    carr.append(c)
        else:
            self.board = board
            self.pch =pch
        self.calculate_moves()
        self.evaluation = self.evaluate()


    def evaluate(self):
        evaluation = 0
        if (self.pch == 'v'):
            return  len(self.vertical_moves()) - len(self.horizontal_moves())
        elif (self.pch == 'h'):
            return  len(self.horizontal_moves()) - len(self.vertical_moves())
        else:
            return 0

    def evaluate_as_target(self):
        return - self.evaluate()


    def calculate_moves(self):
        self.all_moves = []
        if (self.pch == 'v'):
            self.all_moves = self.vertical_moves()
        elif (self.pch == 'h'):
            self.all_moves = self.horizontal_moves()
        else:
            print("INCORRECT COLOR : {}".format(self.pch), file=sys.stderr)
        self.lost =  len(self.all_moves) == 0


    def vertical_moves(self):
        return [(j, i) for j in range(self.ly) for i in range(self.lx) if
                          self.board[j][i] == '-' and j < 7 and self.board[j + 1][i] == '-']

    def horizontal_moves(self):
        return  [(j, i) for j in range(self.ly) for i in range(self.lx) if self.board[j][i] == '-' and i < 7 and self.board[j][i + 1] == '-']




    def execute_move( self, move):
        board_c = deepcopy(self.board)
        if (self.pch == 'v'):
            board_c[move[0]][move[1]] = 'v'
            board_c[move[0]+1][move[1]] = 'v'
        else:
            board_c[move[0]][move[1]] = 'h'
            board_c[move[0]][move[1]+1] = 'v'
        return Position(board=board_c,pch=revert(self.pch))


    def calculate_opp_positions(self):
        opp_positions = []
        for move in self.all_moves:
            opp_position = self.execute_move(move)
            opp_positions.append({"position":opp_position,"move":move})
        return opp_positions

    def dump(self):
        print("=============",file=sys.stderr)
        for b in self.board:
            print("".join(b),file=sys.stderr)
        print("=============",file=sys.stderr)

debug = False

def minmax(position, maximizingPlayer, depth=1, alpha = -math.inf, beta=math.inf):
    debug and print(("   "*depth)+"minmax(depth={}, maximizingPlayer={})".format(depth,maximizingPlayer),file=sys.stderr)
    debug and position.dump()
    if depth == 0:
        return position.evaluate_as_target(), []
    if position.lost or len(position.all_moves) == 0:
        return -math.inf , []
    if (maximizingPlayer):
        bestValue = alpha
        foundMove = None
        for move in position.all_moves:
            new_position = position.execute_move(move)
#            if (new_position.evaluate() < -alpha):
#                continue
            v, pv = minmax(new_position, False, depth-1)

            if (v >= bestValue):
                foundMove = pv + [move]
                debug and print(("   "*depth)+"Adding move : {} {}".format(*move), file=sys.stderr)
                debug and print(("   "*depth)+"Evaluation : {}".format((v)), file=sys.stderr)

                bestValue = max(bestValue, v)
        debug and print(("   " * depth) + "End minmax(depth={}, maximizingPlayer={})".format(depth, maximizingPlayer),
          file=sys.stderr)

        debug and print(("   "*depth)+"Returning bestValue : {} ".format((bestValue)), file=sys.stderr)
        debug and print(("   "*depth)+"Returning foundMove : {} ".format((foundMove)), file=sys.stderr)

        return bestValue, foundMove
    else:
        bestValue = beta
        foundMove = None
        for move in position.all_moves:
            new_position = position.execute_move(move)
#            if (new_position.evaluate() > alpha):
#                continue

            v, pv = minmax(new_position, True  , depth-1  )

            if (v <= bestValue):

                debug and print(("   "*depth)+"Adding move : {} {}".format(*move), file=sys.stderr)
                debug and print(("   "*depth)+"Evaluation : {}".format((v)), file=sys.stderr)

                foundMove = pv + [move]
                bestValue = min(bestValue, v)

        debug and print(("   " * depth) + "End minmax(depth={}, maximizingPlayer={})".format(depth, maximizingPlayer),
              file=sys.stderr)

        debug and print(("   "*depth)+"Returning bestValue : {} ".format((bestValue)), file=sys.stderr)
        debug and print(("   "*depth)+"Returning foundMove : {} ".format((foundMove )), file=sys.stderr)

        return bestValue, foundMove

if __name__ == "__main__":

    position = Position(input=input)
    depth =  3 if (len(position.all_moves) < 10) else 1
    v, pv = minmax(position,  True, depth=depth    , alpha=-3, beta=3)
    if (pv == None):
        v, pv = minmax(position, True, depth=1)

    print(*pv[0])
