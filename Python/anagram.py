def checkAnagram(a, b):
    a_letters = {}
    for letter in a:
        if(letter in a_letters.keys() and letter != ' '):
            a_letters[letter] += 1
        elif (letter != ' '):
            a_letters[letter] = 1
    for letter in b:
        if(letter in a_letters.keys() and letter != ' '):
            a_letters[letter] -= 1
        elif (letter != ' '):
            return False

    for k in a_letters:
        if a_letters[k] != 0:
            return False
    return True

print(checkAnagram("abba","abba"))
