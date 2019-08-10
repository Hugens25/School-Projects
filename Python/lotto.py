import itertools

def check_combo(l):
    for i in range(len(l) - 1):
        if l[i] <= int(l[i+1]/2):
            if i == len(l) - 2:
                return True
                #print("Combo: {}, i: {}, i+1/2: {}".format(combo, combo[i], combo[i+1]/2))
            else:
                continue
        else:
            return False

line = ""
while True:
    count = 1
    line = input()
    idx = 0
    if line == "0 0":
        break

    N = int(line.split()[0])
    M = int(line.split()[1])

    max_list = [0]*N
    min_list = [0]*N
    max_list[N-1] = M
    min_list[0] = 1
    print(max_list)

    for i in range(1,N):
        max_list[N-i-1] = int(max_list[N-i]/2)
        min_list[i] = min_list[i-1]*2
    print(max_list)
    print(min_list)

    while min_list != max_list:
        if max_list[i] < min_list[i-1]*2:


    print(count)
