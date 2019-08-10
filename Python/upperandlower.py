def up_low(str):
    lower = 0
    upper = 0
    for letter in str:
        if not letter.isalpha():
            pass
        elif letter.lower() == letter:
            lower += 1
        else:
            upper += 1
    print(f'There are {lower} lowercase letters and {upper} uppercase letters')

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
