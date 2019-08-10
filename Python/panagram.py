import string
def ispanagram(str, alphabet):
    for letter in str.lower():
        if letter in alphabet:
            alphabet.remove(letter)

    return len(alphabet) == 0
alpha = []
for letter in string.ascii_lowercase:
    alpha.append(letter)
print(ispanagram('The quick brown fox jumps over the lazy dog', alpha))
