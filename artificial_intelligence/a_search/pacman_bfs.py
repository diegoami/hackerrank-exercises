#!/usr/bin/python
state = 0

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


inputarray3 = [
"11 9",
"2 15",
"13 20",
"%%%%%%%%%%%%%%%%%%%%",
"%----%--------%----%",
"%-%%-%-%%--%%-%.%%-%",
"%-%-----%--%-----%-%",
"%-%-%%-%%--%%-%%-%-%",
"%-----------%-%----%",
"%-%----%%%%%%-%--%-%",
"%-%----%----%-%--%-%",
"%-%----%-%%%%-%--%-%",
"%-%-----------%--%-%",
"%-%%-%-%%%%%%-%-%%-%",
"%----%---P----%----%",
"%%%%%%%%%%%%%%%%%%%%"

]



def input():
    global state
    if state < len(inputarray3):
        result = inputarray3[state]
        state += 1
        return result
    else:
        return None



from collections import deque


def walk_idf(maze, sy,sx, y,x):
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


from collections import deque

def walk_bf(maze, sy,sx, y,x):
    S = set()
    Q = deque()

    S.add((sy,sx))
    Q.appendleft((sy,sx))
    max_loops = 500

    exploredPath =  []
    while len(Q) > 0 and max_loops > 0:
        max_loops -= 1
        (cy,cx) = Q.pop()
        exploredPath.append((cy,cx))

        if ((cy,cx) == (y,x)):
            return exploredPath

        else:
            #cand_dirs = [(cy-1,cx),(cy,cx-1),(cy,cx+1),(cy+1,cx)]
            cand_dirs = [(cy - 1, cx), (cy, cx - 1), (cy, cx + 1), (cy + 1, cx)]

            poss_dir = [(j,i) for (j,i) in cand_dirs if 0 < j < len(maze) and  0 < i < len(maze[0]) ]
            for j,i in poss_dir:
                mzchr = maze[j][i]
                if (mzchr != '%' ):
                    if (j,i) not in S:
                        S.add((j,i))
                        Q.appendleft((j,i))


def clean_path(explored_path):
    shortest_path_r = []
    explored_path_r = explored_path[::-1]
    ly, lx = None, None
    for index,(cy,cx) in enumerate(explored_path_r):
        if index == 0:
            shortest_path_r.append((cy,cx))
            ly,lx= cy,cx
        else:
            poss_steps = [(ly + 1, lx), (ly, lx + 1), (ly, lx - 1), (ly - 1, lx)]
            if ((cy,cx) in poss_steps):
                shortest_path_r.append((cy,cx))
                ly,lx =cy,cx

    shortest_path = shortest_path_r[::-1]
    return shortest_path


if __name__ == "__main__":

    maze = []


    sy,sx = map(int,input().split())
    y, x = map(int, input().split())
    ly, lx = map(int, input().split())
    for _ in range(ly):
        maze.append(input())

    exploredPath = walk_bf(maze,sy,sx,y,x)
    print(len(exploredPath))
    for p in exploredPath:
        print(*p, sep=" ")
    addedPath = clean_path(exploredPath)
    print(len(addedPath)-1)
    for p in addedPath:
        print(*p, sep=" ")