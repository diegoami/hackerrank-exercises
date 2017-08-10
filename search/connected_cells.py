
inputarray = [
"4",
"4",
"1 1 0 0",
"0 1 1 0",
"0 0 1 0",
"1 0 0 0"
]
inputarray2 = [

"7",
"5",
"1 1 1 0 1",
"0 0 1 0 0",
"1 1 0 1 0",
"0 1 1 0 0",
"0 0 0 0 0",
"0 1 0 0 0",
"0 0 1 1 0",
]
from tools import input, initArrayInputter
initArrayInputter(inputarray)
from collections import deque
A = []
n = int(input())
m = int(input())
for i in range(n):
    A.append(list(map(int,input().split())))

A1 = [ (i,j) for j in range(len(A[i])) for i in range(len(A)) if A[i][j] == 1  ]
V = set()
areas = {(k1,k2):set([(k1,k2)]) for k1,k2 in A1}
#print(areas)
Q = deque()
for a1 in A1:
    ai,aj = a1
    if a1 not in V:
        Q.append(a1)
        while (len(Q)>0):
            ri,rj = Q.popleft()
            V.add((ri,rj))
            c1= [(bi,bj) for (bi,bj) in A1 if (bi,bj) if (bi,bj) != (ri,rj) and abs(bi-ri) <=1 and abs(bj-rj) <=1  ]
            #print(c1)
            areas[(ri,rj)] = areas[(ri,rj)].union(c1)
            for c in c1:
                areas[c] =  areas[c].union(areas[(ri,rj)])
            Q.extend([x for x in c1 if x not in V])
#print(areas)
print(len(max(areas.items(),key=lambda x: len(x[1]))[1]))


