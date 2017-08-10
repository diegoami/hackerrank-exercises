
inputarray = [
"1",
"2",
"112 42 83 119",
"56 125 56 49",
"15 78 101 43",
"62 98 114 108"
]

from tools import input, initFileInputter
initFileInputter('fp_tc_2.txt')

def input_term():
    global state
    result = inputarray[state]
    state += 1
    return result



q = int(input())
for qx in range(q):
    n = int(input())
    A = []
    for i in range(n*2):
        pl = list(map(int,input().split()))
        A.extend([pl[i:i + n*2] for i in range(0, len(pl), n*2)])

    sum = 0
    #print(n)
    #print(A)
    for y in range(n):
        for x in range(n):
            sum += max([A[y][x],A[2*n-1-y][x],A[y][2*n-1-x],A[2*n-1-y][2*n-1-x]] )

    print(sum)