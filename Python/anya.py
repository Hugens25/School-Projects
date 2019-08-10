num_sentences = int(input())
results = []

def is_palindrome(str):
    return str == str[::-1]

for i in range(num_sentences):
    sentence = input()
    sentence_no_spaces = sentence.replace(' ', '')
    # print(sentence_no_spaces + ' :: ' +sentence_no_spaces[::-1])

    if is_palindrome(sentence_no_spaces):
        results.append('Ay')
        break

    else:
        for word in sentence:
            if is_palindrome(word):
                results.append('Ay')
                break

for result in results:
    print(result)
