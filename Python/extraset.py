#import itertools

def compare_vals(a,b):
    possible_values = [0,1,2]
    possible_values.remove(a)
    possible_values.remove(b)
    #print('Possible Values [0]: {}'.format(possible_values[0]))
    return possible_values[0]

num_cases = int(input())

for i in range(num_cases):
    info = list(map(int, input().split()))
    attributes = info[0]
    total_cards = info[1]
    all_cards = []
    count = 0
    for j in range(total_cards):
        all_cards.append(list(map(int, input().split())))
    #combos = itertools.combinations(all_cards, 2)
    needed_card = []
    for i in range(len(all_cards)):
        for j in range(i+1,len(all_cards)):
            for k in range(attributes):
                possible_values = [0,1,2]
                if all_cards[i][k] == all_cards[j][k]:
                    needed_card.append(all_cards[i][k])

                if all_cards[i][k] != all_cards[j][k]:
                    needed_card.append(compare_vals(all_cards[i][k],all_cards[j][k]))

            #print(needed_card)
            if needed_card in all_cards:
                count += 1
                #print(needed_card)
                needed_card.clear()
            else:
                needed_card.clear()

    print(int(count/3))
