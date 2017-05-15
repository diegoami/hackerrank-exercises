class Tree:
    vertices = {}
    edges = {}
    counter = 0

    def addEdge(self, obj1, obj2):
        edkey= "E" + str(self.counter)
        self.counter += 1
        self.vertices[obj1] = [edkey] if not obj1 in self.vertices else [edkey] + self.vertices[obj1]
        self.vertices[obj2] = [edkey] if not obj2 in self.vertices else [edkey] + self.vertices[obj2]
        self.edges[edkey]=(str(obj1),str(obj2))

    def doPrint(self):
        for v, l in self.vertices.items():
            print(v, l)
        for e,ev in self.edges.items():
            print(e, ev[0], ev[1])

    def walk_node(self,node, walked):
        nl = [node]
        oc = 0
        walked.append(node)
        edges = self.vertices[node]
        for edge in edges:
            tw_node = self.edges[edge][0]
            if (tw_node not in walked):
                rl, roc = self.walk_node(tw_node, walked)
                oc += roc
                nl = nl + rl
                if len(rl) % 2 == 0:
                    oc += 1
        return nl,oc


    def walk_tree(self):
        nl, oc = self.walk_node("1",[])
        return nl, oc





