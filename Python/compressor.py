str = input("Enter a string:")
letters = {}
final_string = ''
single_letters = ''

for c in str:
    try:
        letters[c] += 1
    except:
        letters[c] = 1
        single_letters += c

for i in range(len(single_letters)):
    final_string += (single_letters[i]+'{}'.format(letters[single_letters[i]]))


print(final_string)
