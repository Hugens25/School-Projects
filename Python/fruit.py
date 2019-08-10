from statistics import mean
import math

num_stands = int(input())
day_count = []
most_storage = []

for i in range(num_stands):
    info = input()
    num_fruits = list(map(int, info.split()[1:]))
    avg = int(mean(num_fruits))
    storage = 0
    daily_purchase = avg
    iter = 0
    max_storage = 0
    while iter < len(num_fruits):
        if daily_purchase >= num_fruits[iter]:
            storage += (daily_purchase - num_fruits[iter])
            iter += 1

        elif daily_purchase + storage >= num_fruits[iter]:
            storage = (storage + daily_purchase - num_fruits[iter])
            iter += 1

        elif daily_purchase + storage < num_fruits[iter]:
            daily_purchase += 1
            storage = 0
            max_storage = 0
            iter = iter - 1

        if storage > max_storage:
            max_storage = storage

    day_count.append(daily_purchase)
    most_storage.append(max_storage)

for i in range(len(day_count)):
    print('{} {}'.format(day_count[i], most_storage[i]))
