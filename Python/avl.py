class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.height = 1

class Tree:
    def __init__(self, node):
        self.left_height = 0
        self.right_height = 0
        self.head = node
        # self.left = None
        # self.right = None

    def get_balance(self, head):
        while head != None:
            if head.left != None:
                left_height =  head.left.height
            else:
                left_height = 0
            if head.right != None:
                right_height = head.right.height
            else:
                right_height = 0
            if abs(right_height - left_height > 1):
                return False
            else:
                if head.left != None:
                    self.get_balance(head.left)
                else:
                    break
                if head.right != None:
                    self.get_balance(head.right)
                else:
                    break
        return True

    def get_height(self, head):
        if not head:
            return 0
        return head.height

    def insert(self, head, node):
        if node.data > head.data:
            if head.right == None:
                head.right = node
                #self.right_height += 1
                #print("Head: {} Insert Right: {}.. Right height: {} Left height: {}".format(head.data, node.data, self.right_height, self.left_height))
            else:
                self.insert(head.right, node)
        else:
            if head.left == None:
                head.left = node
                #self.left_height += 1
                #print('Head: {} Insert Left: {}.. Left height: {} Right height: {}'.format(head.data, node.data, self.left_height, self.right_height))
            else:
                self.insert(head.left, node)

        head.height = 1 + max(self.get_height(head.left), self.get_height(head.right))

        # if abs(self.left_height - self.right_height) >= 2:
        #     return False
        # return True
        return self.get_balance(self.head)



num_cases = int(input())
outputs = []

for i in range(num_cases):
    vals = list(map(int, input().split()))
    num_inserts = vals[0]
    inserts = vals[1:len(vals)]
    node = Node(vals[1])
    tree = Tree(node)
    for j in range(1,num_inserts):
        if tree.insert(tree.head, Node(inserts[j])) == False:
            outputs.append('REMOVE')
            break
    outputs.append('KEEP')

for k in range(len(outputs)):
    print('Tree #{}: {}'.format(k+1, outputs[0]))
