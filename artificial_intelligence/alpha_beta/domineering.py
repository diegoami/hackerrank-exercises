from tools import input, initFileInputter
initFileInputter('dom_1.txt')

from random import  randint
def allowed_moves(maze,pch):
    if (pch == 'v'):
        all_cells = [(j, i) for j in range(ly) for i in range(lx) if maze[j][i] == '-' and j < 7 and maze[j+1][i] == '-' ]
    else:
        all_cells = [(j, i) for j in range(ly) for i in range(lx) if maze[j][i] == '-' and i < 7 and maze[j][i+1] == '-' ]

    return all_cells

def execute_move( maze, move, pch):
    pass

if __name__ == "__main__":

    maze = []
    pch = input()

    ly, lx = 8,8
    for _ in range(ly):
        maze.append(input())
    moves = allowed_moves(maze, pch)

    move = moves[randint(1,len(moves))-1]
    print(*move)