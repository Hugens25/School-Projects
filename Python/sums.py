def value_addition(n):
    return sum(range(n+1))

num_datasets = int(input())

for i in range(num_datasets):
    val = int(input())
    Tval = sum([x*value_addition(x+1) for x in range(1,val+1)])
    print("{} {} {}".format(i+1, val, Tval))
