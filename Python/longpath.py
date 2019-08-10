num_cities = int(input())

for i in range(num_cities):
    info = input()
    num_verticies = int(info.split()[0])
    num_edges = int(info.split()[1])
    destination = num_verticies - 1
    connections = {}
    for j in range(num_edges):
        vals = input()
        start = vals.split()[0]
        dest = vals.split()[1]
        mins = vals.split()[2]

        try:
            connections[start].append((dest, mins))
        except:
            connections[start] = []
            connections[start].append((dest, mins))
    print(connections)
