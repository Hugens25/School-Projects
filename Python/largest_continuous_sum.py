def largest_continuous_sum(a):

    max_sum = 0
    current_sum = 0
    start_index = 0
    end_index = 0

    for i in range(len(a)):
        current_sum = max(a[i]+current_sum, a[i])
        max_sum = max(current_sum, max_sum)

        # if a[i] >= current_sum:
        #     start_index = i
        # if max_sum > current_sum:
        #     end_index = i

    return max_sum

print(largest_continuous_sum([1,2,-1,3,4,10,10,-10,-1]))
