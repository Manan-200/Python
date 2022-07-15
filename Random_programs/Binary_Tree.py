class Node:
    def __init__(self, num):
        self.left = None
        self.right = None
        self.val = num
    def traverse(self):
        print(self.val, end = " ")
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()

node_1 = Node(1)
node_1.left = Node(2)
node_1.right = Node(3)
node_1.left.left = Node(4)

node_1.traverse()