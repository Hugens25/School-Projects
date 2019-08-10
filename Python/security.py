import math
from collections import defaultdict

num_cases = int(input())
results = []

for case in range(num_cases):
    rooms = []
    vals = input()
    num_rooms = int(vals.split()[0])
    a = int(vals.split()[1])
    b = int(vals.split()[2])
    mins = []
    map = defaultdict(list)

    for i in range(num_rooms):
        rooms.append(input())

    for i in range(len(rooms)):
        cur_min = 987654321
        #print("In room {}".format(rooms[i]))
        for j in range(i+1, len(rooms)):
            if (i != j):
                dx = abs(int(rooms[j][len(rooms[j])-2:len(rooms[j])]) - int(rooms[i][len(rooms[i])-2:len(rooms[i])]))
                dy = abs(int(rooms[j][0:len(rooms[j])-2]) - int(rooms[i][0:len(rooms[i])-2]))
                time = (a*dx)+(b*dy)
                #print("Function for {} is: {}({}-{}) + {}({}-{}) = {}".format(rooms[j], a, rooms[j][len(rooms[j])-2:len(rooms[j])], rooms[i][len(rooms[i])-2:len(rooms[i])], b, rooms[j][0:len(rooms[j])-2], rooms[i][0:len(rooms[i])-2], time))
                map[rooms[j]].append(time)
                cur_min = min(cur_min, time)

    for m in map:
        #for val in map[m]:
            #print("Map {} has val: {}".format(m, val))
        mins.append(min(map[m]))

    results.append(sum(mins))

for result in results:
    print(result)
