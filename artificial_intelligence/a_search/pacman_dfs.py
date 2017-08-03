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

def input():
    global state
    if state < len(inputarray):
        result = inputarray[state]
        state += 1
        return result
    else:
        return None

from collections import deque
def walk(maze, sy,sx, y,x):
    print("Now walking from {},{} to {}, {} ".format(sy,sx,y,x))
    S = set()
    Q = deque()

    S.add((sy,sx))
    Q.append((sy,sx))
    max_loops = 200
    while len(Q) > 0 and max_loops > 0:
        max_loops -= 1
        (cy,cx) = Q.pop()
        print((cy,cx))
        if ((cy,cx) == (y,x)):
            return (cy,cx)
        else:
            cand_dirs = [(cy-1,cx),(cy,cx-1),(cy,cx+1),(cy+1,cx)]
            poss_dir = [(j,i) for (j,i) in cand_dirs if 0 < j < len(maze) and  0 < i < len(maze[0]) ]
            for j,i in poss_dir:
                mzchr = maze[j][i]
                if (mzchr != '%' ):
                    if (j,i) not in S:
                        S.add((j,i))
                        Q.append((j,i))
    print("Failed")

if __name__ == "__main__":

    pathArray = []
    mazeArray = []


    while True:
        inputString = input()
        if inputString == None:
            break
        if inputString.startswith('%'):
            mazeArray.append(inputString)
        else:
            pathArray.append(tuple(map(int,inputString.split())))


    print(mazeArray)
    print(pathArray)
    sy,sx = 0,0
    for i,path in enumerate(pathArray):

        if i == 0:
            sy,sx = path
        else:
            y,x = path
            walk(mazeArray,sy,sx,y,x)
            sy,sx = y,x


