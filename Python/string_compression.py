import collections

def string_compression(a):

    d = collections.defaultdict(int)
    final_string = ""

    for letter in a:
        d[letter] += 1

    for k,v in d.items():
        final_string += "{}{}".format(k,v)

    return final_string

print(string_compression("AAAAaaaBBBbbCCCCccccCCCDDDEEEFFG"))
