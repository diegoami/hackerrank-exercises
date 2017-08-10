
from tools import input, initArrayInputter
initArrayInputter(inputarray4)

inputarray4 = [
"1",
"10 6",
"3 1",
"10 1",
"10 1",
"3 1",
"1 8",
"5 2",
"3"
]
import collections as col
class Node:
    def __init__(self, ID):
        self.ID = ID
        self.children = []

        self.distance = -1

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID

    def __str__(self):
        return str("{}".format(self.ID))

    def add_child(self,child):

        self.children.append(child)
        child.children.append(self)


class Tree:
    def __init__(self):
        self.idnodes = {}


    def add(self, ID1, ID2):
        if ID1 not in self.idnodes:
            self.idnodes[ID1] = Node(ID1)
        if ID2 not in self.idnodes:
            self.idnodes[ID2] = Node(ID2)
        self.idnodes[ID1].add_child(self.idnodes[ID2])

    def distance(self,ID):
        if ID in self.idnodes:
            return self.idnodes[ID].distance
        else:
            return - 1

    def rewalk(self,  ID):
        if ID not in self.idnodes:
            self.idnodes[ID] = Node(ID)
        self.idnodes[ID].distance = 0
        S = set()
        Q = col.deque()
        S.add(self.idnodes[ID])
        Q.appendleft(self.idnodes[ID])

        while len(Q) > 0:
            current = Q.pop()
            for p in current.children:
                if p not in S:
                    p.distance = current.distance + 6
                    S.add(p)
                    Q.appendleft(p)


n = int(input())
for i in range(n):
    vn,en = map(int,input().split())
    t = Tree()
    for j in range(en):
        v1,v2  = map(int,input().split())
        t.add(v1,v2)
    sn =  int(input())
    t.rewalk (sn)
    vtw = list(range(1,vn+1))
    vtw.remove(sn)
    for v in vtw:
        print(t.distance(v),end=' ')
    print()
