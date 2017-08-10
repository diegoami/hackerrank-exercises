
inputarray = [
"6",
"3",
"5",
"4",
"7",
"2",
"1"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        from collections import deque
        V = set()
        Q = deque()
        Q.append(root)
        while len(Q) > 0:
            c = Q.popleft()
            V.add(c)
            print(c.data,end=' ')
            if c.left:
                Q.append(c.left)
            if c.right:
                Q.append(c.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
