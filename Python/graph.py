class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = []

class Graph:
    # dictionary to access Nodes by their values. ie nodes[2] = Node(2)
    nodes = {}

    # adds node to nodes dictionary. uses key as node id and value as the Node instance
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node.id] = node

    # adds bi-directional edge to graph. remove line 18 for uni-directional
    def add_edge(self, source, dest):
        source.adjacent.append(dest)
        dest.adjacent.append(source)

    def has_path_DFS(self, source, dest, visited):
        print("DFS Checking source: {}, dest: {}".format(source.id, dest.id))
        if source.id in visited:
            return False
        visited.add(source.id)
        if(source == dest):
            return True
        for child in source.adjacent:
            if self.has_path_DFS(child, dest, visited):
                return True
        return False

    def has_path_BFS(self, source, dest):
        next_to_visit = []
        visited = set()
        next_to_visit.append(source)
        while len(next_to_visit) > 0:
            node = next_to_visit[0]
            next_to_visit.pop(0)
            print("BFS Checking node:{} dest:{}".format(node.id, dest.id))
            if node == dest:
                return True
            if node.id in visited:
                continue
            visited.add(node.id)

            for child in node.adjacent:
                next_to_visit.append(child)
        return False        


g = Graph()
nodes = []
for i in range(20):
    nodes.append(Node(i))
    g.add_node(nodes[i])
edges = ['1 2','1 3', '2 4', '2 5', '3 6', '3 7', '4 8']

for edge in edges:
    val1 = int(edge.split()[0])
    val2 = int(edge.split()[1])
    g.add_edge(g.nodes[val1], g.nodes[val2])

print(g.has_path_BFS(nodes[1], nodes[8]))
print(g.has_path_DFS(nodes[1], nodes[8], set()))
