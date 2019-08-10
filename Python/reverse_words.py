def reverse_words(a):
    return " ".join(reversed(a.strip().split()))


def manual_reverse_words(a):
    current_word = ""
    current_words = []
    final_string = ""

    for word in a:
        if word == " ":
            current_words.append(current_word)
            current_word = ""
            continue
        current_word += word
    current_words.append(current_word)

    for word in current_words:
        if word != "":
            final_string = word+" "+final_string

    return final_string

#print(reverse_words("Hi John,    are you ready to go?"))
print(manual_reverse_words("   Hi John,    are you ready to go?"))
