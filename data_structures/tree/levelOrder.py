state = 0

inputarray = [
"47 2 49 1 40 48 50 20 44 14 38 43 45 10 16 30 39 41 46 7 12 15 19 28 31 42 5 9 11 13 17 27 29 34 3 6 8 18 21 33 35 4 25 32 36 22 26 37 24 23"
]

sol = [
"47 2 40 20 38 30 14 28 10 16 19 44 39 27 7 9 31 12 43 21 5 41 34 49 13 33 3 4 25 22 29 15 32 35 6 24 23 26 1 11 42 36 37 17 18 8 45 48 50 46"
]

from collections import deque
def input():
    global state
    result = inputarray[state]
    state += 1
    return result


"""
     1
    /  \
       2
        \
         5
        /  \
       3    6
        \
         4
def tree1() :
    ns = {}
    for i in range(1,7):
        ns[i] = Node(i)
    t = Tree(ns[1])

    ns[1].add_right(ns[2])
    ns[2].add_right(ns[5])
    ns[5].add_right(ns[6])
    ns[5].add_left(ns[3])
    ns[3].add_left(ns[4])
    return t

"""

from data_structures.tree.btree import *

from collections import deque

def scan(node):
    res = []
    VU = set()
    Q = deque()
    Q.appendleft(node)
    while (len(Q) > 0):
        cnode = Q.pop()
        if cnode not in VU:
            VU.add(cnode)
            res.append(str(cnode.data))
            if cnode.left:
                Q.appendleft(cnode.left)
            if cnode.right:
                Q.appendleft(cnode.right)

    return res

def levelOrder(root):
    print(" ".join(scan(root)))

lm = list(map(int, input().strip().split(' ')))
tree = BinarySearchTree()


for le in lm:
    tree.create(le)
levelOrder(tree.root)
