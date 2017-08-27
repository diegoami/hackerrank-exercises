import sys
import os


def find_exit(maze):
    for j in range(len(maze)):
        if 'e' in maze[j]:
            return (j,maze[j].index('e'))
    return None

dirs = ['UP','RIGHT','DOWN','LEFT']
def turn_dir(orig_dir, prev_dir):
    prev_dir_index = dirs.index(prev_dir)
    orig_dir_index = dirs.index(orig_dir)
    while prev_dir_index > 0:
        orig_dir_index -= 1
        prev_dir_index -= 1
        if orig_dir_index == -1:
            orig_dir_index = 3
    return dirs[orig_dir_index]

def turn_maze(maze , prev_dir):
    turns = dirs.index(prev_dir)
    new_maze = maze

    for _ in range(turns):
        new_maze = [ ['-','-','-'], ['-','-','-'], ['-','-','-']]
        for j in range(3):
            for i in range(3):
                new_maze[i][j] = maze[2-j][i]

        maze = new_maze
    return new_maze




def get_best_move(maze, dir="UP"):

    def walk_possible(maze, dir):
        if dir == 'DOWN' and maze[2][1] == '-':
            return True
        elif dir == 'RIGHT' and maze[1][2] == '-':
            return True
        elif dir == 'UP' and maze[0][1] == '-':
            return True
        elif dir == 'LEFT' and maze[1][0] == '-':
            return True


    exit = find_exit(maze)
    if (exit):
        if exit[0] == 2:
            return 'DOWN'
        elif exit[0] == 0:
            return 'UP'
        elif exit[1] == 0:
            return 'LEFT'
        else:
            return 'RIGHT'
    else:
        while True:
            if walk_possible(maze,dir):
                return dir
            dir_index = dirs.index(dir)
            dir_index = dir_index - 1 if dir_index > 0 else 3
            dir = dirs[dir_index]
filename = "myfile.txt"

def read_direction():
    if (os.path.isfile(filename)):
        with open( filename, "r") as f:
            lines = f.readlines()
            if (len(lines) > 0):
                return (lines[0].split(','))
            else:
                return "UP","UP"
    else:
        return "UP","UP"


def write_direction(dir,orig_dir):
    with open(filename, "w") as f:
        f.write(dir+","+orig_dir)

def process(input):
    player = int(input())
    maze = []
    for j in range(3):
        maze.append([])
    for j in range(3):

        mazej = input()
        for i in range(3):
            maze[j].append(mazej[i])
    prev_dir, prev_norm_dir = read_direction()
    print("======PREV_DIR === {} == {} =======".format(prev_dir,prev_norm_dir), file=sys.stderr)


    new_maze = turn_maze(maze,prev_norm_dir)
    #print(maze)
    print("======NORMAL MAZE === ", file=sys.stderr)
    print(new_maze,file=sys.stderr)

    orig_dir = get_best_move(new_maze,prev_norm_dir)
    new_dir = turn_dir(orig_dir, prev_dir)
    print("======NEW DIR === {} == {}== ".format(new_dir, orig_dir), file=sys.stderr)

    write_direction(new_dir, orig_dir)
    print(new_dir)

def do_test_inputs():
    from tools import input, initFileInputter
    for i in range(2,3,1):
        str_to_pr = 'maze_'+str(i)+'.txt'
        print("======PROCESSING === {} ==========".format(str_to_pr),file=sys.stderr)
        initFileInputter(str_to_pr)
        process(input)
        print("======  END PROCESSING === {} =======".format(str_to_pr), file=sys.stderr)


def test_mazes():

    maze = [['#', '#', '#'], ['#', '-', '-'], ['#', '-', '-']]
    new_maze = turn_maze(maze,'RIGHT')
    print(new_maze)

    maze = [['-', '-', '#'], ['-', '-', '#'], ['#', '#', '#']]
    new_maze = turn_maze(maze, 'LEFT')
    print(new_maze)

    maze = [['#', '-', '-'], ['#', '-', '-'], ['#', '#', '#']]
    new_maze = turn_maze(maze, 'DOWN')
    print(new_maze)


if __name__ == "__main__":
    #do_test_inputs()
    #new_maze = do_turn_maze('')
    process(input)
    #test_mazes()