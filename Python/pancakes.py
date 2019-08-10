num_cases = int(input())
total_plates = []

for i in range(num_cases):
    num_inputs = int(input())
    plates = 1
    cur_plates = []

    line = list(map(int, input().split()))
    for k in range(1,len(line)):
        if line[k] >= line[k-1] and line[k-1] != 0:
            #print("if line[k]:{} line[k-1]:{}".format(line[k], line[k-1]))
            plates += 1

        elif line[k] == 0 and k != len(line)-1:
            #print("elif line[k]:{} line[k-1]:{}".format(line[k], line[k-1]))
            plates += 1

    total_plates.append(plates)

for plate in total_plates:
    print(plate)


#2 4 22 0 3 4 0 5 6 0
