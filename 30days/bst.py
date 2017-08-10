
inputarray = [
"7",
"3",
"5",
"2",
"1",
"4",
"6",
"7"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

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

    def getHeight(self, root):
        if (root.left == None and root.right == None):
            return 0
        elif (root.left == None):
            return 1+self.getHeight(root.right)
        elif (root.right == None):
            return 1 + self.getHeight(root.left)
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


# Write your code here

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)