import itertools

num_cases = 1
max_sums = []

while num_cases != 0:
    num_cases = int(input())
    profit_sums = []
    #profit_sums.append(0)
    total_profits = []

    for i in range(num_cases):
        todays_profit = int(input())
        if(todays_profit != 0):
            total_profits.append(todays_profit)
            profit_sums.append(todays_profit)

    for i in range(len(total_profits)):
        for j in range(len(total_profits)):
            profit_sums.append(sum(total_profits[i:j+1]))

    # if 0 in profit_sums:
    #     profit_sums.remove(0)
    if len(profit_sums) > 0:
        max_sums.append(max(profit_sums))
for sum in max_sums:
    print(sum)
