num_passwords = int(input())
passwords = []

for i in range(num_passwords):
    password = ''
    indicies = []
    letters = []
    len_password = int(input())

    for j in range(len_password):
        cur_letters = input()
        letters.append(cur_letters)
        indicies.append(len(cur_letters))

    desired_idx = int(input()) - 1

    for i in range(len(indicies) - 1, -1, -1):
        prev_idx = indicies[i]
        indicies[i] = (desired_idx % indicies[i])
        #print('\n {} % {} = {}'.format(str(desired_idx), str(prev_idx), str(int(indicies[i]))))
        password = letters[i][indicies[i]] + password
        #print('\n {} / {} = {}'.format(str(desired_idx), str(prev_idx), str(int(desired_idx / prev_idx))))
        desired_idx = (int(desired_idx / prev_idx))

    passwords.append(password)

for password in passwords:
    print(password.strip())
