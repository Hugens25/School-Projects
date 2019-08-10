num_cases = int(input())

for i in range(num_cases):
    lowest_floor = 0
    floors = []
    floors.append(0)
    directions = input()
    for letter in directions:
        if letter == "^":
            lowest_floor += 1
            floors.append(lowest_floor)
        if letter == "v":
            lowest_floor -= 1
            floors.append(lowest_floor)
    print(abs(min(floors)))
