state = 0
inputarray = [
"5"
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result

class CNode:

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.distance = None
        self.children = []

    def add_child(self,child):
        self.children.append(child)

    def get_poss_moves(self,a,b,n):
        pmoves = []
        for i,j in [(self.x+a,self.y+b),(self.x+b,self.y+a),(self.x-a,self.y+b),(self.x-b,self.y+a),(self.x+a,self.y-b),(self.x+b,self.y-a),(self.x-a,self.y-b),(self.x-b,self.y-a)]:
                if (0 <= i < n) and (0 <= j < n):
                    pmoves.append((i,j))
        return pmoves

    def path_to_end(self):
        lpath= []
        lstart = self
        while lstart.path is not None:
            lpath.append([(lstart.x,lstart.y)])
            lstart = lstart.path
        return lpath

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

    def do_search(self, wnode):
        cntLvl = 0
        fndEnd = None
        while fndEnd is None and cntLvl < 1000:
            #wnode.distance = None
            #wnode.path     = None
            #for x in self.visited:
            #    x.distance = None
            #    x.path     = None
            self.visited = []
            fndEnd = self.search(wnode,cntLvl)
            if fndEnd is not None:
                return cntLvl, fndEnd
            else:
                cntLvl += 1
        return -1, None

    def search(self, wnode,lvl):

        if wnode not in self.visited:
            self.visited.append(wnode)
            if (wnode.x == self.dx) and (wnode.y == self.dy):
                wnode.distance = 0
                wnode.path =  [(wnode.x,wnode.y)]
               # print(wnode)
                return wnode

            if lvl > 0:
                pmoves = wnode.get_poss_moves(self.a, self.b, self.n)
                #print(pmoves)
                for p in pmoves:
                    pnode = CNode(p[0], p[1])
                    fndNode = self.search(pnode,lvl-1)
                    if fndNode is not None:
                        wnode.distance = fndNode.distance + 1
                        wnode.path     =  [(wnode.x,wnode.y)]+fndNode .path
                        #print(wnode)
                        return wnode
            else:
                return None
        else:
            return None
def do_walk(x,y,a,b,n):

    cnode = CNode(x,y)
    ctree = CTree(cnode,a,b,n)
    rst,fndend = ctree.do_search(cnode)
    #rst,fndend = 3,ctree.search(cnode,3)
    return rst
    #print("LVL :"+str(rst))
#    if fndend is not None:
#        print(fndend.path, fndend.distance)


#do_walk(0,0,1,1,5)
"""
do_walk(0,0,1,2,5)
do_walk(0,0,1,3,5)
do_walk(0,0,1,4,5)
do_walk(1,1,1,4,5)



"""
nb = int(input())
for i in range(1,nb):
    rl = []
    for j in range(1,nb):
        rl.append(str(do_walk(0,0,i,j,nb)))
    print(" ".join(rl))



"""
def search(self, wnode):
    print("Searching node " + str(wnode))
    if wnode not in self.visited:
        self.visited.append(wnode)
        if (wnode.x == self.dx) and (wnode.y == self.dy):
            wnode.distance = 0
            print("Returning node " + str(wnode))
            return wnode
        else:
            pmoves = wnode.get_poss_moves(self.a, self.b, self.n)
            print("Pmoves = " + str(pmoves))
            for p in pmoves:
                pnode = CNode(p[0], p[1])
                if pnode in self.visited:
                    pnodeidx = self.visited.index(pnode)
                    pnode = self.visited[pnodeidx]
                if (pnode.x == self.dx) and (pnode.y == self.dy):
                    pnode.distance = 0
                    wnode.distance = 1

                    print("Returning node " + str(wnode))
                    return wnode
                if pnode not in wnode.children:
                    wnode.add_child(pnode)
            for pnode in wnode.children:
                self.search(pnode)
            nnone = [x for x in wnode.children if x.distance is not None]
            if (len(nnone) > 0):
                min_node = min(nnone, key=lambda x: x.distance)
                wnode.distance = min_node.distance + 1
            print("Returning node " + str(wnode))
            return wnode

    else:
        wnodeidx = self.visited.index(wnode)
        wnode = self.visited[wnodeidx]
        print("Returning node " + str(wnode))
        return wnode

"""
"""

def search(self, wnode, lvl):
    # print("Searching node " + str(wnode) + " at lvl "+str(lvl))
    if wnode not in self.visited:
        self.visited.append(wnode)
        # else:
        #   wnodeidx = self.visited.index(wnode)
        #   wnode = self.visited[wnodeidx]
        if (wnode.x == self.dx) and (wnode.y == self.dy):
            wnode.distance = 0
            wnode.path = [(wnode.x, wnode.y)]
            # print(" Found wnode " + str(wnode))
            return wnode

        if lvl > 0:
            pmoves = wnode.get_poss_moves(self.a, self.b, self.n)
            # print("Pmoves = " + str(pmoves))
            for p in pmoves:
                pnode = CNode(p[0], p[1])
                # if pnode in self.visited:
                #     pnodeidx = self.visited.index(pnode)
                #     pnode = self.visited[pnodeidx]
                # if pnode.distance is not None:
                #     wnode.distance =  pnode.distance+1
                #     wnode.path     =  [(wnode.x,wnode.y)]+pnode.path
                # print(" Found wnode " + str(wnode))

                fndNode = self.search(pnode, lvl - 1)
                if fndNode is not None:
                    wnode.distance = fndNode.distance + 1
                    wnode.path = [(wnode.x, wnode.y)] + fndNode.path

        else:
            return None
        
"""