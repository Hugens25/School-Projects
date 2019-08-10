class Node:

    def __init__(self, n):
        self.left = None
        self.right = None
        self.data = n

    def insert(self, value):
        if value <= self.data:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left != None:
                self.left.contains(value)
            else:
                return False
        else:
            if self.right != None:
                self.right.contains(value)
            else:
                return False

    def in_order_traversal(self):
        if self.left != None:
            self.left.in_order_traversal()

        print(self.data)

        if self.right != None:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.data)

        if self.left != None:
            self.left.in_order_traversal()

        if self.right != None:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left != None:
            self.left.in_order_traversal()

        if self.right != None:
            self.right.in_order_traversal()

        print(self.data)


tree = Node(7)
tree.insert(6)
tree.insert(8)
tree.insert(10)
tree.insert(2)
print('Pre-Order')
tree.pre_order_traversal()
print("In-Order")
tree.in_order_traversal()
print('Post-Order')
tree.post_order_traversal()
