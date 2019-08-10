import itertools

num_cases = int(input())

for i in range(num_cases):
    info = list(map(int, input().split()))
    attributes = info[0]
    total_cards = info[1]
    all_cards = []
    count = 0
    for j in range(total_cards):
        all_cards.append(list(map(int, input().split())))
    combos = itertools.combinations(all_cards, 2)
    for combo in combos:
        needed_card = []
        for k in range(attributes):
            possible_values = [0,1,2]
            if (combo[0][k] == combo[1][k]):
                needed_card.append(combo[0][k])
            if (combo[0][k] != combo[1][k]):
                possible_values.remove(combo[0][k])
                possible_values.remove(combo[1][k])
                needed_card.append(possible_values[0])
        if needed_card in all_cards:
            count += 1
            #print(needed_card)
    print(int(count/3))
