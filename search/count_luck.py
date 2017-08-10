
inputarray = [
"3",
"2 3",
"*.M",
".X.",
"1",
"4 11",
".X.X......X",
".X*.X.XXX.X",
".XX.X.XM...",
"......XXXX.",
"3",
"4 11",
".X.X......X",
".X*.X.XXX.X",
".XX.X.XM...",
"......XXXX.",
"4"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray)
from collections import deque

def find_exit(A,RH,PK,n,m):
    PW = {RH:0}
    V = set()

    Q = deque()
    Q.append(RH)
    while (len(Q) > 0):
        (y,x) = Q.popleft()
        V.add((y,x))
        CW = PW[(y,x)]
        if (y,x) == PK:
            return PW
        V.add((y,x))
        cl = [(yi, xi) for (yi, xi) in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)] if xi >=0 and yi >=0 and yi < n and xi < m and A[yi][xi] in ['.','*'] and (yi,xi) not in V ]
        mpnt= len(cl) > 1
        for c in cl:
            Q.append(c)
            PW[c] = CW+1 if mpnt else CW

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    A = []
    RH, PK = (0,0), (0,0)
    for j in range(n):
        Aj = input()
        if Aj.find('*') > -1:
            PK = (j,Aj.find('*'))
        if Aj.find('M') > -1:
            RH = (j, Aj.find('M'))
        A.append(Aj)
    PW = find_exit(A,RH,PK,n,m)

    r = int(input())
    print("Impressed" if PW[PK] == r else "Oops!")