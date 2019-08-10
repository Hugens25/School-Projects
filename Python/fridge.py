vals = input()

num_bottles = int(vals.split()[0])
max_height = int(vals.split()[1])
bottle_heights = input().split()
bottle_heights = sorted(bottle_heights)[::-1]

left_height = 0
right_height = 0
bottle_count = 0

for i in range(len(bottle_heights)):
    if i % 2 == 0:
        left_height += int(bottle_heights[i])
        bottle_count += 1
    else:
        right_height += int(bottle_heights[i])
        bottle_count += 1

    if left_height > max_height:
        left_height -= int(bottle_heights[i])
        bottle_count -= 1
    if right_height > max_height:
        right_height -= int(bottle_heights[i])
        bottle_count -= 1

print(bottle_count)
