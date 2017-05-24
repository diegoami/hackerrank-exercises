state = 1
import linecache
def input():
    global state
    result = linecache.getline('testcase_1.txt', state)
    state += 1
    return result

from collections import deque
class AdjMatrix:
    def __init__(self,n,m,cl,cr):
        self.A = []
        self.C = {}
        for i in range(n):
            Ai = []
            self.A.append(Ai)
            for j in range(n):
                self.A[i].append(0)

        self.cr = cr
        self.cl = cl

    def add_city(self,city_1,city_2):
        self.A[city_1][city_2] = 1
        self.A[city_2][city_1] = 1

    def get_adjacent(self,n):
        return self.a[n]

    def graph(self):
        return self.A

    def conn(self):
        return [x[1] for x in self.C.items() if len(x[1]) > 1]

    def cost(self):
        if self.cr >= self.cl:
            return len(self.A)*self.cl
        else:
            tl, tr =self.walk_graph()
            return tl*self.cl + tr*self.cr


    def walk_graph(self):
        GVU = set()
        tl, tr = 0, 0
        for i in range(len(self.A)):
            if i in GVU:
                continue
            tl += 1
            VU = set()
            S = deque()
            S.append(i)
            while (len(S) > 0):
                v = S.pop()
                if v not in VU and v not in GVU:
                    VU.add(v)
                    GVU.add(v)
                    for j,Aj in enumerate(self.A[v]):
                        if Aj > 0 and v != j:
                            S.append(j)

            tr += len(VU)-1
        return (tl,tr)

q = int(input().strip())
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    Aj = AdjMatrix(n,m,x,y)
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        Aj.add_city(city_1-1,city_2-1)

    print(Aj.cost())



