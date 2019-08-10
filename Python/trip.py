num_cases = int(input())
prices = []

for i in range(num_cases):
    vals = input().split()

    adult_price = float(vals[0])
    child_price = float(vals[1])
    num_adults = float(vals[2])
    num_child = float(vals[3])

    prices.append((adult_price * num_adults) + (child_price * num_child))

for price in prices:
    print("{:.2f}".format(price))
