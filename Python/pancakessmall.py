num_cases = int(input())
total_plates = []

def div_by_two(x):
    return int(x/2)

for i in range(num_cases):
    num_inputs = int(input())
    plates = 1
    cur_plates = []

    line = list(map(int, input().split()))
    print(line)
    line = list(map(div_by_two, line))
    print(line)
    for k in range(1,len(line)):
        if line[k] >= line[k-1]:
            plates += 1

    total_plates.append(plates)

for plate in total_plates:
    print(plate)


#2 4 22 1 3 4 7 5 6 0
