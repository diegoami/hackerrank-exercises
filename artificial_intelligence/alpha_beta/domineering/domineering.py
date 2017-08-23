from tools import input, initFileInputter
initFileInputter('dom_2.txt')

from copy import deepcopy
from random import  randint
import sys



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


class Node:

    def __init__(self, position, parent_edge=None, depth=0):
        self.position = position
        self.parent_edge = parent_edge
        self.children = []
        self.valid_edges = []
        self.depth = depth
        self.lost = position.lost
        self.best_edge = None
        self.won = False



    def add_position(self, move, child_position):
        child =  Edge(self.position, move, child_position)
        self.children.append(child)

    def retrieve_positions(self):
        opp_positions = self.position.calculate_opp_positions()
        for opp in opp_positions:
            new_position = Node(opp["position"], self.depth + 1)

            self.add_position(opp["move"], new_position )


    def evaluate(self):
        for edge in self.children:
            self.valid_edges.append(edge)

            if (edge.end_node.position.lost):
                print("FOUND WINNING MOVE : {} {}".format(*edge.move), file=sys.stderr)
                self.best_edge = edge
                self.won = True
                self.valid_edges.append(edge)
                break
            elif (edge.end_node.won):
                print("FOUND LOSING MOVE : {} {}".format(*edge.move), file=sys.stderr)
                continue


        if (len(self.valid_edges) > 0):
            self.valid_edges = sorted(self.valid_edges, key=lambda e: e.end_node.position.evaluate_as_target(), reverse=True)
            for edge in self.valid_edges:
                print(" MOVE {} {}, EVALUATION {} ".format(edge.move[0], edge.move[1], edge.end_node.position.evaluate_as_target()),
                      file=sys.stderr)

            self.best_edge = self.valid_edges[0]


class Edge:

    def __init__ (self, origin_node, move, end_node):
        self.origin_node = origin_node
        self.move = move
        self.end_node = end_node

class PositionTree:

    def __init__(self, position) :
        self.root_node = Node(position)
        self.create_tree()
        self.evaluate_tree()

    def create_tree(self):


        self.root_node.retrieve_positions()

    def evaluate_tree(self):
        self.root_node.evaluate()


    def choose_move(self):
        if (self.root_node.best_edge):
            return self.root_node.best_edge.move
        else:
            edge = self.root_node.valid_edges[0]
            #edge = self.rootNode.valid_edges [randint(1, len(self.rootNode.valid_edges )) - 1]
            #print("NO WINNING MOVE, RANDOM MOVE {} {}".format(*edge.move), file=sys.stderr)

            print("NO WINNING MOVE, PICKING FIRST MOVE{} {}".format(*edge.move), file=sys.stderr)

            return edge.move


if __name__ == "__main__":

    position = Position(input=input)
    positionTree = PositionTree(position)
    move = positionTree.choose_move()
    print(*move)