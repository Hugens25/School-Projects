def array_pair_sum(lst, num):

    equals_num = []

    for item1 in lst:
        for item2 in lst:
            if item1 + item2 == num and (item2, item1) not in equals_num:
                equals_num.append((item1, item2))

    return len(equals_num)


def optimized_array_pair_sum(lst, num):

    equals_num = set()
    seen = set()

    for item in lst:
        target = num - item
        if target in seen and (target, item) not in equals_num:
            equals_num.add((item, target))
        seen.add(item)

    return len(equals_num)

print(optimized_array_pair_sum([1,3,2,2,4,0,3], 6))
