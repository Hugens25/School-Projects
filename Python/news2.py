num_cases = int(input())

for i in range(num_cases):
    num_employees = int(input())
    structure = input().replace(" ", "")
    length_of_calls = 1
    in_call = [[]]
    for j in range(1,len(structure)):
        if structure[j] in in_call:
            length_of_calls += 1
        else:
            in_call.append(structure[j])
