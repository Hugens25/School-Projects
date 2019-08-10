def mergestrings(a,b):

    # find the minimum length of both
    # strings so that we know when to
    # stop traversing in for loop
    min_len = min(len(a), len(b))

    # set the bigger word to a, but check
    # if b is longer than a. If so, assign
    # max_word to b.
    max_word = a

    if len(a) < len(b):
        max_word = b

    merged_string = ""

    # add each character in both words to
    # merged_string until we reach the end
    # of the smallest string's characters,
    # once we get to the end, append the
    # remaining characters of the larger
    # string onto the merged_string variable.
    for i in range(min_len):
        merged_string += a[i] + b[i]

    merged_string += max_word[i+1:]

    return merged_string

print(mergestrings('abcde', 'xyz'))
