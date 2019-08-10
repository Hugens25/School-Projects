output = ''
i = 1
word1 = input()
same = False
word1_list = []
word2_list = []

while(True):
    word2 = input()
    if word2 == "END":
        break
    if len(word1) == len(word2):
        for letter in word1:
            word1_list.append(letter)
        for letter in word2:
            word2_list.append(letter)
        word1_list.sort()
        word2_list.sort()

        if word1_list == word2_list:
            output += 'Case {}: same\n'.format(i)
        else:
            output += 'Case {}: different\n'.format(i)
    else:
        output += 'Case {}: different\n'.format(i)
    i += 1
    word1_list = []
    word2_list = []
    word1 = input()

print(output)
