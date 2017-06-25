"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def scan(node):
    return [str(node.data)] + scan(node.left) + scan(node.right) if node else []


def preOrder(root):
    print(" ".join(scan(root)))

