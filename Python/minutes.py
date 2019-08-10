num_repititions = int(input())
mins = []

for i in range(num_repititions):
    values = input()
    standard_values = [1440, 60, 1]
    given_values = [int(values.split()[0]), int(values.split()[1]), int(values.split()[2])]
    total_mins = sum([a*b for a,b in zip(standard_values, given_values)])
    mins.append(total_mins)

for min in mins:
    print(min)
