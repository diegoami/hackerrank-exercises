



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



from itertools import product

class Position:
    holes = [1, 2, 3, 4, 5, 6]
    players = ['1', '2']


    moves_1 = list(product(['1'],holes))
    moves_2 = list(product(['2'],holes))

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
        ev = self.board['1']['mancala']-self.board['2']['mancala'] + ( 2 if self.board['N'] == '1' else -2)
        ev += (sum(self.board['1']['holes']) - sum(self.board['2']['holes']))/5
        return ev

    def evaluate_as_target(self):
        return - self.evaluate()

    def evaluate_as_obs(self):
        return self.evaluate() if self.pch == '1' else -self.evaluate()

    def calculate_moves(self):
        self.all_moves = []

        if (self.board['N']  == '1'):
            self.all_moves = [s for s in self.moves_1 if self.board['1']['holes'][s[1]-1] > 0]

        elif (self.board['N'] == '2'):
            self.all_moves = [s for s in self.moves_2 if self.board['2']['holes'][s[1]-1] > 0]
        else:
            print("INCORRECT COLOR : {}".format(self.pch), file=sys.stderr)


    def execute_move(self, moveTot):
        def get_marbles_in_hole(board, player, hole):
            return board[player]['holes'][hole - 1]

        def set_marbles_in_hole(board, player, hole, value):
            board[player]['holes'][hole - 1] = value

        def inc_marbles_in_hole(board, player, hole, delta):
            board[player]['holes'][hole - 1] += delta

        move = moveTot[1]
        board_c = deepcopy(self.board)

        player, other_player = board_c['N'], revert(board_c['N'])
        marbles = get_marbles_in_hole(board_c, player, move)
        set_marbles_in_hole(board_c, player, move, 0)
        curr_hole = move
        while marbles > 0:
            curr_hole += 1
            real_hole = curr_hole % 14
            if (real_hole == 0):
                pass
            elif real_hole  <= 6:
                inc_marbles_in_hole(board_c, player, real_hole , 1)
                marbles -= 1
            elif real_hole  == 7:
                board_c[player]['mancala'] += 1
                marbles -= 1
            elif real_hole  < 14:
                inc_marbles_in_hole(board_c, other_player, real_hole-7, 1)
                marbles -= 1
            else:
                pass



        if (curr_hole < 7 ) and get_marbles_in_hole(board_c, player, curr_hole) == 1:
            inc_marbles_in_hole(board_c, player, curr_hole, get_marbles_in_hole(board_c, other_player, 7-curr_hole))
            set_marbles_in_hole(board_c, other_player, 7-curr_hole, 0)


        if (curr_hole != 7):
            board_c['N'] = other_player

        return Position(board=board_c,pch=self.pch)


    def calculate_opp_positions(self):
        opp_positions = []
        for move in self.all_moves:
            opp_position = self.execute_move(move)
            opp_positions.append({"position":opp_position,"move":move})
        return opp_positions

    def dump(self):
        f = {"file" : sys.stderr}
        print("============== POSITION ==================",**f)
        print("{}".format(self.board['N']),**f)
        print("{}".format(self.board['1']['mancala']),**f)
        print(*self.board['1']['holes'],sep=' ', **f)
        print("{}".format(self.board['2']['mancala']),**f)
        print(*self.board['2']['holes'],sep=' ', **f)
        print("============EVALUATION : {} =============".format(self.evaluate_as_obs()), **f)
        print("===========END POSITION ==================",**f)


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



def process(input):
    position = Position(input=input)
    position.dump()
    opp_positions  = position.calculate_opp_positions()
    ops = sorted(opp_positions, key=lambda x: x['position'].evaluate_as_obs(), reverse = True)
    for o in ops:
        print("==== MOVE === : {} {} ".format(*o['move']),file=sys.stderr)
        o['position'].dump()
    print(ops[0]['move'][1])


def do_test_inputs():
    from tools import input, initFileInputter
    for i in range(1,5,1):
        str_to_pr = 'manca_'+str(i)+'.txt'
        print("======PROCESSING === {} ==========".format(str_to_pr),file=sys.stderr)
        initFileInputter('manca_'+str(i)+'.txt')
        process(input)
        print("======  END PROCESSING === {} =======".format(str_to_pr), file=sys.stderr)


if __name__ == "__main__":
    #process(input)
    do_test_inputs()