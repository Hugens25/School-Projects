class Queue:

    def __init__(self):
        self.q = []
        self.count = 0

    def enqueue(self, item):
        self.q.append(item)
        self.count += 1

    def dequeue(self):
        removed_element = self.q[0]
        self.q.pop(0)
        self.count -= 1
        return removed_element

    def size(self):
        return(self.count)

    def isEmpty(self):
        return self.count == 0


q = Queue()
q.enqueue(5)
q.enqueue(6)
print(q.size())
print(q.isEmpty())
print("Removing: {}".format(q.dequeue()))
print(q.size())
print(q.isEmpty())
print("Removing: {}".format(q.dequeue()))
print(q.size())
print(q.isEmpty())
