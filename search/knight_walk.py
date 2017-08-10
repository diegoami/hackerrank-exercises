
inputarray = [
"5"
]
import collections as col
from tools import input, initArrayInputter
initArrayInputter(inputarray)

class CNode:

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.distance = None
        self.parent = None


    def get_poss_moves(self,a,b,n):
        pmoves = []
        for i,j in [(self.x+a,self.y+b),(self.x+b,self.y+a),(self.x-a,self.y+b),(self.x-b,self.y+a),(self.x+a,self.y-b),(self.x+b,self.y-a),(self.x-a,self.y-b),(self.x-b,self.y-a)]:
                if (0 <= i < n) and (0 <= j < n):
                    if (i,j) not in pmoves:
                        pmoves.append((i,j))
        return pmoves

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str("{},{} : {}".format(self.x, self.y, self.distance))


class CTree:


    def __init__(self,cnode,a,b,n):
        self.root = cnode
        self.a    = a
        self.b    = b
        self.n    = n
        self.dx   = n-1
        self.dy   = n-1
        self.visited = []


    def do_search(self, node):

        S = set()
        Q = col.deque()
        S.add(node)
        Q.appendleft(node)

        while len(Q) > 0:
            current = Q.pop()
            #print(current)
            if current.x == self.dx and current.y == self.dy:
                current.distance = 0
                lpnode = current
                while lpnode is not None:
                    if (lpnode.parent):
                        lpnode.parent.distance = lpnode.distance + 1
                        lpnode = lpnode.parent
                    else:
                        lpnode = None
                return current
            else:
                pmoves = current.get_poss_moves(self.a,self.b,self.n)
                for p in pmoves:
                    pnode = CNode(p[0],p[1])
                    if pnode not in S:
                        S.add(pnode)
                        pnode.parent = current
                        Q.appendleft(pnode)


def do_walk(x,y,a,b,n):

    cnode = CNode(x,y)
    ctree = CTree(cnode,a,b,n)
    fnode = ctree.do_search(cnode)
    return cnode.distance if cnode.distance is not None else -1




nb = int(input())
for i in range(1,nb):
    rl = []
    for j in range(1,nb):
        rl.append(str(do_walk(0,0,i,j,nb)))
    print(" ".join(rl))

