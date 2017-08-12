from tools import input, initFileInputter
initFileInputter('dom_3.txt')

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

def allowed_moves(maze,pch):
    all_cells = []
    if (pch == 'v'):
        all_cells = [(j, i) for j in range(ly) for i in range(lx) if maze[j][i] == '-' and j < 7 and maze[j+1][i] == '-' ]
    elif (pch == 'h'):
        all_cells = [(j, i) for j in range(ly) for i in range(lx) if maze[j][i] == '-' and i < 7 and maze[j][i+1] == '-' ]
    else:
        print("INCORRECT COLOR : {}".format(pch), file=sys.stderr)
    return all_cells

def execute_move( maze, move, pch):
    maze_c = deepcopy(maze)
    #print(maze_c)
    if (pch == 'v'):
        maze_c[move[0]][move[1]] = 'v'
        maze_c[move[0]+1][move[1]] = 'v'
    else:
        maze_c[move[0]][move[1]] = 'h'
        maze_c[move[0]][move[1]+1] = 'v'
    return maze

def find_winning_move(maze_eval):
    for move in maze_eval["moves"]:
        maze_opp = execute_move(maze, move, pch)
        maze_eval_opp = analyze(maze_opp, revert(pch))
        if (maze_eval_opp["lost"]):

            return move
    return None



def analyze(maze, pch):
    moves = allowed_moves(maze,pch)
    lost = len(moves) == 0
    return {"moves" : moves, "lost" : lost, "pch" : pch}

if __name__ == "__main__":

    maze = []
    pch = input()

    ly, lx = 8,8
    for _ in range(ly):
        carr = []
        maze.append(carr )
        cl = input()
        for c in cl:
            carr.append(c)
    maze_eval = analyze(maze, pch)
    if (maze_eval["lost"]):
        print("lost")
    else:
        winning_move = find_winning_move(maze_eval)
        if (winning_move):
            print("FOUND WINNING MOVE : {} {}".format(winning_move[0], winning_move[1]), file=sys.stderr)
            print(*winning_move)
        else:
            print("NO WINNING MOVE, RANDOM MOVE", file=sys.stderr)

            moves = maze_eval["moves"]
            if (len(moves) > 0):
                move = moves[randint(1,len(moves))-1]
                print(*move)
            else:
                print("NO VALID MOVE, WE LOSE")