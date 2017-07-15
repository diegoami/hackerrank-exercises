state = 0

inputarray = [
"10",
"1 1 2 2",
"4 3 5 2",
"2 4 5 6",
"1 2 2 2",
"1 1 1 1",
"1 2 2 1",
"1 8 7 8",
"9 1 1 1",
"8 4 3 2",
"7 8 9 1"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result



n = int(input())
for i in range(n):
    px, py, qx, qy = map(int, input().split())
    dx, dy = (qx - px), (qy - py)
    rx, ry = qx + dx , qy +  dy
    print(int(rx),int(ry))