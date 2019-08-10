def cube(n):
    return n*n*n

num_list = []
for num in range(101):
    if num > 50 and num % 5 == 0:
        continue;
    num_list.append(num)

print(num_list)

result = map(cube, num_list)
num_list = list(result)
total_result = []

for num in num_list:
    if num % 2 == 0:
        continue;
    total_result.append(num)

print(total_result)
