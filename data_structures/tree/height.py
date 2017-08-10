

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

inputarray2 = [
"3",
"3",
"5",
"2",
]


from tools import input, initArrayInputter
initArrayInputter(inputarray)



class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
import sys

def height(root):
    if (root.left == None and root.right == None):
        return 0
    hl = height(root.left) if root.left else 0
    hr = height(root.right) if root.right else 0
    heightTot = max(hl,hr)+1
    print("Node {} : (hl,hr) : ( {}, {} ) : heightTot : {}".format(root.info,hl,hr,heightTot), file=sys.stderr)
    return heightTot


tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)

print(height(tree.root))

