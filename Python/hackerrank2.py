import random

def maxDifference(a):

  diff_list = []
  for i in range(len(a)):
    if i == 0:
      continue
    if(a[i] > min(a[:i])):
      diff_list.append(a[i] - min(a[:i]))

  if len(diff_list) > 0:
    return max(diff_list)
  return -1

random_nums = random.sample(range(-1000000, 1000000), 20000)

print(maxDifference(random_nums))
