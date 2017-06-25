"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def scan(node):
    return scan(node.left) + [str(node.data)] +   scan(node.right) if node else []


def inOrder(root):
    print(" ".join(scan(root)))

