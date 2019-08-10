import random

def rand_num(low, high, n):
    for i in range(n):
        yield random.randrange(low,high)

print(list(rand_num(2,20,3)))
