state = 0
inputArray = [
"r",
"4 3 5 13",
"###############",
"#-rr--------gg#",
"#-rr--------gg#",
"#-rr--------gg#",
"#-rr--------gg#",
"#-r---------g-#",
"#-r---------gg#",
"#rr----------g#",
"#-------------#",
"#-------------#",
"#-------------#",
"#-------------#",
"#-------------#",
"#-------------#",
"###############",
]

inputArray2 = [
"g",
"4 3 5 13",
"###############",
"#-rr--------gg#",
"#-rr--------gg#",
"#-rr--------gg#",
"#-rr--------gg#",
"#-r---------g-#",
"#-r---------gg#",
"#rr----------g#",
"#-------------#",
"#-------------#",
"#-------------#",
"#-------------#",
"#-------------#",
"#-------------#",
"###############",
]


def input():
    global state
    if state < len(inputArray2):
        result = inputArray2[state]
        state += 1
        return result
    else:
        return None


import math
import sys

def heuristic_cost_estimate(sy,sx,y,x,ty,tx):
    cost = distance_between(sy, sx, y, x)
    if (ty,tx) == (y,x):
        cost -= 1
    return cost


def distance_between(sy, sx, y, x):
    return abs(sy - y) + abs(sx - x)


def dict_infinity(mj,mi):
    return {(j,i) : math.inf for j in range(mj) for i in range(mi)}



def reconstruct_path(cameFrom, cy,cx):
    total_path = [(cy,cx)]
    total_steps = 0
    while (cy,cx) in cameFrom:
        (cy, cx) = cameFrom[(cy, cx)]
        total_path.append((cy, cx))
        total_steps += 1
    return total_path, total_steps


def neighbors(maze,cy,cx):
    cand_dirs = [(cy - 1, cx), (cy, cx - 1), (cy, cx + 1), (cy + 1, cx)]
    poss_dir = [(j, i) for (j, i) in cand_dirs if 0 < j < len(maze) and 0 < i < len(maze[0]) and maze[j][i] == '-']
    return poss_dir

def walk_astar(maze, ly, lx, sy, sx, y, x):
    print("Finding path from {}, {} to {}, {}".format(sy,sx,y,x),file=sys.stderr)
    closedSet, openSet = set(), set([(sy,sx)])
    cameFrom = {}
    gScore, fScore = dict_infinity(ly,lx), dict_infinity(ly,lx)
    gScore[(sy,sx)] = 0
    fScore[(sy,sx)] = heuristic_cost_estimate(sy,sx,y,x,y,x)
    MAX_LOOPS = 1000
    n_loops = 0
    while len(openSet) > 0 and n_loops < MAX_LOOPS :
        n_loops += 1
        cy, cx = min(openSet, key=lambda x: fScore[x])
        if (cy,cx) == (y,x):
            path, steps = reconstruct_path(cameFrom, cy, cx)

            return path[::-1],steps

        openSet.remove((cy,cx))
        closedSet.add((cy,cx))
        for (ny,nx) in neighbors(maze,cy,cx):
            if (ny,nx) in closedSet:
                continue
            if (ny,nx) not in openSet:
                openSet.add((ny,nx))

            tentative_gscore = gScore[(cy,cx)] + (0 if (cy,cx) == (y,x) else 1)
            if tentative_gscore > gScore[(ny,nx)]:
                continue
            cameFrom[(ny,nx)] = (cy,cx)
            gScore  [(ny,nx)] = tentative_gscore
            fScore  [(ny,nx)] = gScore[(ny,nx)] + heuristic_cost_estimate(ny,nx,y,x,y,x)

    return None, math.inf


def is_red(maze,j,i):
    return maze[j][i] == 'r'

def is_green(maze,j,i):
    return maze[j][i] == 'g'

def matching_cells(maze,ly,lx,func):
    return [(j,i) for j in range(ly) for i in range(lx) if func(maze,j,i)]

def dict_calc(maze, all_cells, func, **kwargs):
    return {(j,i) : func(maze,j,i, **kwargs) for (j,i) in all_cells}

def dist_to_cells(maze,j,i,**kwargs):

    cells_to_avoid = kwargs["cells_to_avoid"]
    nj, ni = min(cells_to_avoid, key=lambda c : abs(j-c[0])+abs(i-c[1]))
    return abs(nj-j)+abs(ni-i)



def red_cells(maze,ly,lx):
    return matching_cells(maze,ly,lx, is_red)

def green_cells(maze,ly,lx):
    return matching_cells(maze,ly,lx, is_green)


def get_direction(sy, sx, ny, nx):
    if ny == sy - 1:
        return "UP"
    elif ny == sy + 1:
        return "DOWN"
    elif nx == sx - 1:
        return "LEFT"
    elif nx == sx + 1:
        return "RIGHT"
    return None


if __name__ == "__main__":

    maze = []
    pch = input()
    ry,rx,gy,gx = map(int,input().split())

    sy,sx = (ry,rx) if pch == 'r' else (gy,gx)
    ly, lx = 15,15
    for _ in range(ly):
        maze.append(input())
    all_cells = [(j,i) for j in range(ly) for i in range(lx) if maze[j][i] != '#']
    rcs = red_cells(maze,ly,lx)
    gcs =  green_cells(maze, ly, lx)
    red_dist_dict = dict_calc(maze, all_cells, dist_to_cells, cells_to_avoid=rcs)
    green_dist_dict = dict_calc(maze, all_cells, dist_to_cells, cells_to_avoid=gcs)
    all_dist_dict =     dict_calc(maze, all_cells, dist_to_cells, cells_to_avoid=gcs+rcs)
    possible_targets = sorted(all_dist_dict.items(), key = lambda x : x[1], reverse=True)

    for k,v in possible_targets:
        y,x = k
        print("Tring target {}, {}".format(y,x), file=sys.stderr)
        path, steps = walk_astar(maze,ly,lx,sy,sx,y,x)
        if path != None and len(path) > 1:
            ny, nx = path[1]
            print("Going to {}, {}".format(ny, nx), file=sys.stderr)
            direction = get_direction(sy, sx, ny, nx)
            print("Direction : {}".format(direction), file=sys.stderr)
            print(direction)
            break
    print("WE LOSE",file=sys.stderr)