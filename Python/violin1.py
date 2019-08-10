# 0 0 4 4 1 3 1 2 1 4 0 0 0
#
# 0 0 4 0 3 1 1 1 1 1 2 0 0
#
# 0 0 4 0 3 1 1 1 1 1 0 0 0 = 12
#
# 0 0 1 0 2 1 1 1 1 1 0 0 0

num_strings = int(input())
strings = []
totals = []

for i in range(num_strings):
    stack = []
    total = 0
    strings = input().split()[1:]
    num_times_played = {}
    #print('Strings: {}'.format(strings))

    for string in strings:
        string = int(string)
        #print('Stack: {}'.format(stack))
        if string == 0 and len(stack) == 0:
            #print('Empty with 0 entry, total is: {}'.format(total))
            continue

        if string == 0:
            while len(stack) > 0:
                total += 1
                #print('Popping {} because 0 entry. Total is {}'.format(stack[len(stack) - 1], total))
                stack.pop()
            continue

        if len(stack) == 0:
            stack.append(string)
            total += 1
            #print('Adding {} to stack. Total is {}'.format(string, total))
            continue

        if string == stack[len(stack) - 1]:
            #print('String is same as stack. Not adding anything. Total is {}'.format(total))
            continue

        if string > stack[len(stack) - 1]:
            stack.append(string)
            total += 1
            #print('Adding {} to stack because it is greater than {}. Total is {}'.format(string, stack[len(stack) - 1], total))
            continue

        if string < stack[len(stack) - 1]:
            while len(stack) > 0 and string < stack[len(stack) - 1]:
                total += 1
                #print('{} is greater than {}, so popping off stack. Total is: {}'.format(stack[len(stack) - 1], string, total))
                stack.pop(len(stack) - 1)
            if len(stack) == 0 or string > stack[len(stack) - 1]:
                stack.append(string)
                total += 1
                #print('Adding {} because stack is empty or {} is bigger than {}'.format(string, string, stack[len(stack) - 1]))
            if len(stack) - 1 > 0 and string != stack[len(stack) - 1]:
                stack.append(string)
                total += 1
                #print('Adding {} becuase it is not equal to {}. Total is {}'.format(string, stack[len(stack) - 1], total))
    #print(stack)
    totals.append(total)
for total in totals:
    print(total)
