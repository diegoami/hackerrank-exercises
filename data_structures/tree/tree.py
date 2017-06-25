


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self,leftNode):
        self.left = leftNode

    def add_right(self, rightNode):
        self.right = rightNode

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self,root):
        self.root = root


