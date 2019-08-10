import math

num_cases = int(input())
total_counts = []

for i in range(num_cases):
    count = 0
    values = input().split()
    num = int(values[0])
    full_range = int(values[1])

    for i in range(1,full_range+1):
        if math.gcd(num, i) == 1:
            count += 1
    total_counts.append(count)

for c in total_counts:
    print(c)
