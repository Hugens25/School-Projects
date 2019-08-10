import collections

def find_missing_element(a, b):

    a = sorted(a)
    b = sorted(b)

    for i in range(len(a)):
        if i == len(b) or a[i] != b[i]:
            return a[i]

    return "Lists are identical"



def optimized_find_missing_element(a, b):

    d = collections.defaultdict(int)

    for element in b:
        d[element] += 1

    for element in a:
        if d[element] == 0:
            return element
        else:
            d[element] -= 1

print("{} is the missing element".format(optimized_find_missing_element([1,2,3,4,5,6,7], [3,5,4,6,7,1])))
