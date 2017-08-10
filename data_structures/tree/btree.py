from collections import deque




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 0

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
            self.root.level = 0
        else:
            current = self.root
            clevel = 1
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                        clevel = clevel+1
                    else:
                        current.left = Node(val)
                        current.left.level = clevel
                        break
                elif val > current.data:
                    if current.right:
                        clevel = clevel + 1
                        current = current.right
                    else:
                        current.right = Node(val)
                        current.right.level = clevel
                        break
                else:
                    break

    def scan(self,func, *funcargs):

        VU = set()
        Q = deque()
        Q.appendleft(self.root)
        while (len(Q) > 0):
            cnode = Q.pop()
            if cnode not in VU:
                VU.add(cnode)
                func(cnode,*funcargs)
                if cnode.left:
                    Q.appendleft(cnode.left)
                if cnode.right:
                    Q.appendleft(cnode.right)

    def preOrder(self,node, func, *funcargs):
        if node is not None:
            func(node, *funcargs)
        return [str(node.data)] + self.preOrder(node.left, func, *funcargs) + self.preOrder(node.right, func, *funcargs) if node else []

    def inOrder(self,node, func, *funcargs):
        if node is not None:
            irno = self.inOrder(node.left, func, *funcargs)
            func(node, *funcargs)
            return irno + [str(node.data)] + self.inOrder(node.right, func, *funcargs)
        else:
            return []

    def pnode(self,cnode,*funcargs):
        if cnode is not None:
            print(cnode.level*" "+str(cnode.data))


    def printPreOrder(self):
        self.preOrder(self.root, self.pnode)

    def printInOrder(self):
        self.inOrder(self.root, self.pnode)

    def print(self):
        self.scan(self.pnode)

if __name__ == '__main__':



    inputarray = [
        "47 2 49 1 40 48 50 20 44 14 38 43 45 10 16 30 39 41 46 7 12 15 19 28 31 42 5 9 11 13 17 27 29 34 3 6 8 18 21 33 35 4 25 32 36 22 26 37 24 23"
    ]

    from collections import deque


    from tools import input, initArrayInputter
    initArrayInputter(inputarray)

    res = []
    def fres(cnode,l):
        l.append(str(cnode.data))


    lm = list(map(int, input().strip().split(' ')))
    tree = BinarySearchTree()


    for le in lm:
        tree.create(le)
    #tree.scan(fres,res)
    #print(res)
    #tree.print()
    tree.printInOrder()
    #tree.printPreOrder()
