num_cases = int(input())

for i in range(num_cases):
    num_employees = int(input())
    structure = input().replace(" ", "")
    length_of_calls = 1
    already_made_calls = []
    batch = []
    batch.append([])
    for j in range(1,len(structure)):
        if structure[j] not in already_made_calls:
            already_made_calls.append(structure[j])
        #if structure[j] == structure[j-1] or int(structure[j-1]) == j - 1:
        if structure[j] == structure[j-1] or int(structure[j]) < j+1:
            print("Adding call because structure[j-1]: {} and structure[j]: {}".format(structure[j-1], structure[j]))
            length_of_calls += 1

    print(length_of_calls)
