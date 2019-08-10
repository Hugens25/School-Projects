num_cases = int(input())
l = []

for i in range(num_cases):
    students_locations = input().split()
    num_locations = int(students_locations[0])
    num_students = int(students_locations[1])
    initial_capacities = list(map(int, input().split()))
    capacities = initial_capacities
    buffer = min(capacities)

    capacities = [x - buffer for x in capacities]
    if sum(capacities) > num_students:
        l.append(min(initial_capacities))
        continue
    while(sum(capacities) < num_students):
        capacities = [x + 1 for x in capacities]

    print("{} - {}".format(min(initial_capacities), min(capacities)))
    l.append(min(initial_capacities) - min(capacities))
for el in l:
    print(el)

# 2
# 4 35
# 6 10 25 15
# 2 57
# 20 40
