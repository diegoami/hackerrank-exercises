state = 1
import linecache
def input():
    global state
    result = linecache.getline('jm_2.txt', state)
    state += 1
    return result

from collections import deque
from itertools import combinations

class AdjMatrix:

    def __init__(self,n,m):
        self.A = {k:[] for k in range(0,n)}
        self.n  = n
        self.m  = m
        self.VUS = []

    def get_connections(self,v):
        return self.A[v]

    def add_edge(self, edge_1, edge_2):
        self.A[edge_1].append(edge_2)
        self.A[edge_2].append(edge_1)

    def cost(self):
        clstrs,singles = self.walk_graph()
        #print(clstrs)
        cmbs   = combinations(clstrs,2)
        ptys   = sum([x*y for (x,y) in cmbs])+(singles*(singles-1))/2+sum([x*singles for x in clstrs])
        return ptys

    def walk_graph(self):
        GVU = set()
        clstr,singles = [],0
        for i in range(n):
            if i in GVU:
                continue
            VU = set()
            S = deque()
            S.append(i)
            while (len(S) > 0):
                v = S.pop()
                if v not in VU and v not in GVU:
                    VU.add(v)
                    GVU.add(v)
                    S.extend(self.get_connections(v))
            if (len(VU) >  1):
                clstr.append(len(VU))
            else:
                singles += 1
        return clstr, singles

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
Aj = AdjMatrix(n,m)
for a1 in range(m):
    edge_1, edge_2 = input().strip().split(' ')
    edge_1, edge_2 = [int(edge_1),int(edge_2)]
    Aj.add_edge(edge_1, edge_2)
print(int(Aj.cost()))



