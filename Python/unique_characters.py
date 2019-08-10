def unique_characters(s):
    chars = []

    for character in s:
        if character in chars:
            return False
        chars.append(character)
    return True

print(unique_characters("abcde"))
