num_votes = int(input())
total_votes = {}
max_vote = 0

for i in range(num_votes):
    name = input().strip()
    try:
        total_votes[name] += 1
    except:
        total_votes[name] = 1

    if total_votes[name] > max_vote:
        max_vote = total_votes[name]

winners = []
for vote in total_votes:
    if total_votes[vote] == max_vote:
        winners.append(vote)

winners.sort()

for winner in winners:
    print(winner)
