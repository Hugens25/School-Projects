num_maps = int(input())
results = []
visited = []

def find_val(l, idx, target):
    if idx < len(l) and l[idx] == []:
        visited[idx] = True
        return
    if target in l[idx]:
        visited[idx] = True
        results.append(1)
        return
    for element in l[idx]:
        if(visited[element] != True):
            visited[element] = True
            find_val(l, element, target)

for i in range(num_maps):
    trials = []
    routes = []
    num_trials = int(input())
    for j in range(num_trials):
        trials.append(input())
    map_info = input().split()
    num_locations = int(map_info[0])
    target = num_locations - 1
    num_routes = int(map_info[1])
    for num in range(num_routes):
        routes.append([])
    for val in range(num_locations):
        visited.append([])
    for k in range(num_routes):
        possible_routes = input().split()
        if possible_routes[2] not in trials:
            routes[int(possible_routes[0])].append(int(possible_routes[1]))
            routes[int(possible_routes[1])].append(int(possible_routes[0]))
    find_val(routes, 0, target)
    if len(results) == 0:
        results.append(0)
    else:
        if i < len(results) and results[i] == 1:
            continue
        else:
            results.append(0)
    #print(routes)
for result in results:
    print(result)
