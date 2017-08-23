from tools import input, initFileInputter
initFileInputter('dom_7.txt')





from copy import deepcopy
from random import  randint
import sys
import math

def revert(pch):
    if (pch == '1'):
        return '2'
    elif (pch == '2'):
        return '1'
    else:
        print("INCORRECT COLOR : {}".format(pch), file=sys.stderr)
        return pch

class Position:


    def __init__(self, input=None, board=None, pch=None):
        self.board = {}

        self.board['1'] = {"mancala" : 0, "holes" : []}
        self.board['2'] = {"mancala" : 0, "holes" : []}
        self.board['N'] = '1'
        if (input):
            self.pch = input()
            self.board['1']['mancala'] = int(input())
            self.board['1']['holes'] = list(map(int, input().split()))
            self.board['2']['mancala'] = int(input())
            self.board['2']['holes'] = list(map(int, input().split()))
            self.board['N'] = self.pch
        else:
            self.board = board
            self.pch =pch
        self.calculate_moves()
        self.evaluation = self.evaluate()


    def evaluate(self):
        evaluation = 1 if self.pch ==  self.board['N'] else 0
        if (self.pch == '1'):
            return self.board['1']['mancala']-self.board['2']['mancala']
        elif (self.pch == '2'):
            return self.board['2']['mancala']-self.board['1']['mancala']
        else:
            print("INCORRECT COLOR : {}".format(self.pch), file=sys.stderr)
            return 0

    def evaluate_as_target(self):
        return - self.evaluate()


    def calculate_moves(self):
        self.all_moves = []
        if (self.pch == '1'):
            return [1,2,3,4,5,6]
        elif (self.pch == '2'):
            return [1,2,3,4,5,6]
        else:
            print("INCORRECT COLOR : {}".format(self.pch), file=sys.stderr)
            return []

    def execute_move(self, move):
        board_c = deepcopy(self.board)
        player, other_player = self.board_c['N'], revert(self.board_c['N'])
        marbles = self.board_c[player]['holes'][move]
        self.board_c[player]['holes'][move] = 0
        curr_hole = move
        while marbles > 0:
            curr_hole += 1
            if curr_hole <= 6:
                self.board_c[player]['holes'][curr_hole] += 1
            elif curr_hole == 7:
                self.board_c[player]['mancala'] += 1
            else:
                self.board_c[other_player]['holes'][curr_hole-6] += 1
            marbles -= 1
        if (curr_hole < 7 ) and self.board_c[player]['holes'][curr_hole] == 1:
            self.board_c[player]['holes'][curr_hole] += self.board_c[other_player]['holes'][7-curr_hole]
            self.board_c[other_player]['holes'][7 - curr_hole] = 0

        if (curr_hole != 7):
            self.board_c['N'] = other_player






debug = True

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
    v, pv = minmax(position,  True, depth=1)
