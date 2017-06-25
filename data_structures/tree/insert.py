state = 0

inputarray = [
"5",
"4 2 3 1 7",
"6"
]


from collections import deque
def input():
    global state
    result = inputarray[state]
    state += 1
    return result




"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

from data_structures.tree.btree import *
from data_structures.tree.levelOrder import levelOrder


def insert(r, val):
    if r == None:
        r = Node(val)
    else:
        current = r
        while True:
            if val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            elif val > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    current.right.level = clevel
                    break
            else:
                break
    return r

n = int(input())
lm = list(map(int, input().strip().split(' ')))
na = int(input())
tree = BinarySearchTree()
for le in lm:
    tree.create(le)
insert(tree.root,na)
tree.printInOrder()