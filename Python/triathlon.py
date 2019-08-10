from operator import itemgetter, attrgetter

num_races = int(input())
results = []

def sort_list(l):
    for item in l:
        item = tup(item)
    sorted(l, key=lambda item: item[3])
    return l

for i in range(num_races):
    competitors = []
    race_info = input().split()
    num_runners = int(race_info[0])
    miles_for_swim = float(race_info[1])
    miles_for_bike = float(race_info[2])
    miles_for_run = float(race_info[3])

    for i in range(num_runners):
        cur_competitor = []
        runner_info = input().split()
        cur_competitor.append(runner_info[0])
        cur_competitor.append(runner_info[1])
        cur_competitor.append(int(runner_info[2]))
        swim_time = miles_for_swim/float(runner_info[3])*60
        bike_time = miles_for_bike/float(runner_info[4])*60
        run_time = miles_for_run/float(runner_info[5])*60
        cur_competitor.append((swim_time+bike_time+run_time)/60)
        competitors.append(cur_competitor)
    competitors = sorted(competitors, key=itemgetter(3,2,1,0))
    results.append(competitors)

i = 1
for result in results:
    print("Race {}:".format(i))
    i += 1
    for competitor in result:
        print('{} {} {}'.format(competitor[0],competitor[1],format(competitor[3],'.3f')))
    print('')
