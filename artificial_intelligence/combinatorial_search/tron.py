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

def input():
    global state
    if state < len(inputArray):
        result = inputArray[state]
        state += 1
        return result
    else:
        return None

def is_red(maze,j,i):
    return maze[j][i] == 'r'

def is_green(maze,j,i):
    return maze[j][i] == 'g'

def matching_cells(maze,ly,lx,func):
    return [(j,i) for j in range(ly) for i in range(lx) if func(maze,j,i)]

def red_cells(maze,ly,lx):
    return matching_cells(maze,ly,lx, is_red)

def green_cells(maze,ly,lx):
    return matching_cells(maze,ly,lx, is_green)

if __name__ == "__main__":

    maze = []
    pch = input()
    ry,rx,gy,gx = map(int,input().split())

    ly, lx = 15,15
    for _ in range(ly):
        maze.append(input())
    print(red_cells(maze,ly,lx))
    print(green_cells(maze, ly, lx))


