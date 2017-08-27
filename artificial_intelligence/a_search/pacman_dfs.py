#!/usr/bin/python


inputarray = [
"3 9",
"5 1",
"7 20",
"%%%%%%%%%%%%%%%%%%%%",
"%--------------%---%",
"%-%%-%%-%%-%%-%%-%-%",
"%--------P-------%-%",
"%%%%%%%%%%%%%%%%%%-%",
"%.-----------------%",
"%%%%%%%%%%%%%%%%%%%%"
]

inputarray2 = [
"25 13",
"3 1",
"27 28",
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%",
"%------------%%------------%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%.%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%--------------------------%",
"%-%%%%-%%-%%%%%%%%-%%-%%%%-%",
"%-%%%%-%%-%%%%%%%%-%%-%%%%-%",
"%------%%----%%----%%------%",
"%%%%%%-%%%%%-%%-%%%%%-%%%%%%",
"%%%%%%-%%%%%-%%-%%%%%-%%%%%%",
"%%%%%%-%------------%-%%%%%%",
"%%%%%%-%-%%%%--%%%%-%-%%%%%%",
"%--------%--------%--------%",
"%%%%%%-%-%%%%%%%%%%-%-%%%%%%",
"%%%%%%-%------------%-%%%%%%",
"%%%%%%-%-%%%%%%%%%%-%-%%%%%%",
"%------------%%------------%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%---%%----------------%%---%",
"%%%-%%-%%-%%%%%%%%-%%-%%-%%%",
"%%%-%%-%%-%%%%%%%%-%%-%%-%%%",
"%------%%----%%----%%------%",
"%-%%%%%%%%%%-%%-%%%%%%%%%%-%",
"%------------P-------------%",
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
]

"""
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%",
"%------------%%------------%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%.%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%--------------------------%",
"%-%%%%-%%-%%%%%%%%-%%-%%%%-%",
"%-%%%%-%%-%%%%%%%%-%%-%%%%-%",
"%------%%----%%----%%------%",
"%%%%%%-%%%%%-%%-%%%%%-%%%%%%",
"%%%%%%-%%%%%-%%-%%%%%-%%%%%%",
"%%%%%%-%------------%-%%%%%%",
"%%%%%%-%-%%%%--%%%%-%-%%%%%%",
"%--------%--------%--------%",
"%%%%%%-%-%%%%%%%%%%-%-%%%%%%",
"%%%%%%-%------------%-%%%%%%",
"%%%%%%-%-%%%%%%%%%%-%-%%%%%%",
"%------------%%------------%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%-%%%%-%%%%%-%%-%%%%%-%%%%-%",
"%---%%------------XXXX%%---%",
"%%%-%%-%%-%%%%%%%%X%%X%%-%%%",
"%%%-%%-%%-%%%%%%%%X%%X%%-%%%",
"%------%%----%%XXXX%%XXXXXX%",
"%-%%%%%%%%%%-%%-%%%%%%%%%%X%",
"%------------PXXXXXXXXXXXXX%",
"%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
]

"""

from tools import input, initArrayInputter
initArrayInputter(inputarray2)


from collections import deque
def walk(maze, sy,sx, y,x):
    S = set()
    Q = deque()

    S.add((sy,sx))
    Q.append((sy,sx))
    max_loops = 500


    exploredPath =  []
    while len(Q) > 0 and max_loops > 0:
        max_loops -= 1
        (cy,cx) = Q.pop()
        exploredPath.append((cy,cx))

        if ((cy,cx) == (y,x)):
            return exploredPath
        else:
            cand_dirs = [(cy-1,cx),(cy,cx-1),(cy,cx+1),(cy+1,cx)]
            poss_dir = [(j,i) for (j,i) in cand_dirs if 0 < j < len(maze) and  0 < i < len(maze[0]) ]
            for j,i in poss_dir:
                mzchr = maze[j][i]
                if (mzchr != '%' ):
                    if (j,i) not in S:
                        S.add((j,i))
                        Q.append((j,i))

def clean_path(explored_path):
    shortest_path = []
    for index,(cy,cx) in enumerate(explored_path):
        s_dirs = [(cy + 1, cx), (cy, cx + 1), (cy, cx - 1), (cy - 1, cx)]
        if len(shortest_path) > 0:
            py, px = shortest_path[-1]
            s_dirs = [(cy,cx) for (cy,cx) in s_dirs if (cy,cx) != (py,px)]
        for s_dir in s_dirs:
            if s_dir in shortest_path:
                shortest_path =  shortest_path[:shortest_path.index(s_dir)+1]
        shortest_path.append((cy,cx))

    return shortest_path
if __name__ == "__main__":

    maze = []


    sy,sx = map(int,input().split())
    y, x = map(int, input().split())
    ly, lx = map(int, input().split())
    for _ in range(ly):
        maze.append(input())

    exploredPath = walk(maze,sy,sx,y,x)
    print(len(exploredPath))
    for p in exploredPath:
        print(*p, sep=" ")
    addedPath = clean_path(exploredPath)
    print(len(addedPath)-1)
    for p in addedPath:
        print(*p, sep=" ")