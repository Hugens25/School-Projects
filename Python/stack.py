class Stack:

    def __init__(self):
        self.count = 0
        self.stack = []

    def push(self, a):
        self.stack.insert(0, a)
        self.count += 1

    def pop(self):
        removed_value = self.stack[0]
        self.stack.pop(0)
        self.count -= 1
        return removed_value

    def peek(self):
        return self.stack[0]

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

s = Stack()
s.push(3)
s.push(4)
print(s.peek())
print("Removing: {}".format(s.pop()))
print(s.peek())
print(s.isEmpty())
print(s.size())
