from tools import input, initFileInputter
initFileInputter('testcase_3.txt')


from collections import deque
class AdjMatrix:

    def __init__(self,n,m,cl,cr):
        self.A = {k:[] for k in range(1,n+1)}
        self.cr = cr
        self.cl = cl
        self.n  = n
        self.VUS = []

    def get_connections(self,v):
        return self.A[v]

    def add_city(self,city_1,city_2):
        self.A[city_1].append(city_2)
        self.A[city_2].append(city_1)

    def cost(self):
        if self.cr >= self.cl:
            return n*self.cl
        else:
            tl, tr =self.walk_graph()
            return tl*self.cl + tr*self.cr

    def walk_graph(self):
        GVU = set()
        tl, tr = 0, 0
        for i in range(1,n+1):
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
                    S.extend(self.get_connections(v))
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
        Aj.add_city(city_1,city_2)

    print(Aj.cost())



