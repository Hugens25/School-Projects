num_cases = int(input())
outputs = []
datasets = []

for i in range(num_cases):
    info = input().split()
    num_set = info[0]
    val = info[1]
    begin = ''
    end = ''
    finish = False

    # keep track of this dataset number in list
    datasets.append(num_set)

    if len(val) == 1:
        outputs.append("BIGGEST")
    else:

        # traverse input srting from last index to first index.
        for j in range(len(val)-1, 0, -1):
            # if value at current position is greater than value at left position
            # set this as our breaking point. Our begin string will consist of
            # the substring from 0 to this point, and the end of our string will
            # consist of the substring from this point to the end of the string.
            # NOTE: In order to get next largest number in sequence, we need to
            # find a value that is greater-than or equal to the value after our
            # break point. Store this compareing value in compare_val.
            if val[j] > val[j-1]:
                begin = val[:j-1]
                end = val[j-1:]
                compare_val = end[0]
                break

            # if we are still in our for loop and j is at the beginning index,
            # that means this is the largest permutation of this string, as all
            # the decimal values are in descending order. Set finish flag to True
            # so that we do not contunie into if-statement.

            if j - 1 == 0:
                outputs.append("BIGGEST")
                finish = True

        if not finish:
            # Sort the end of our string (EXCLUDING our compare_val). Find the next
            # value that is greater-than or equal to compare_val and append to begin
            # string. Remove that value from end string, add our compare_val, then resort.
            # Append each element to begin string.
            sorted_end = ''.join(sorted(end[1:]))
            for k in range(len(sorted_end)):
                if sorted_end[k] >= compare_val:
                    begin += sorted_end[k]
                    sorted_end = sorted_end[:k] + sorted_end[k+1:]
                    sorted_end += compare_val
                    sorted_end = ''.join(sorted(sorted_end))
                    for e in sorted_end:
                        begin += e
                    outputs.append(begin)
                    break

for num in range(len(outputs)):
    print("{} {}".format(datasets[num], outputs[num]))
