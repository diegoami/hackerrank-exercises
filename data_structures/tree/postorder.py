"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def scan(node):
    return scan(node.left) +  scan(node.right) + [str(node.data)]  if node else []


def postOrder(root):
    print(" ".join(scan(root)))

