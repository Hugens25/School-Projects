l = [1,3,2,3,6]

for element in range(len(l) - 1):
    if l[element] == 3 and l[element - 1] == 3:
        print('True')


print('False')
