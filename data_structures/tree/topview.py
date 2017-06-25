"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""



def scan_left(node):
    return scan_left(node.left) + [str(node.data)]  if node else []

def scan_right(node):
    return [str(node.data)]+scan_right(node.right)  if node else []

def topView(root):
    tpl = scan_left(root.left)
    tpr = scan_right(root.right)
    print(" ".join(tpl+[str(root.data)] +tpr))

  #Write your code here


