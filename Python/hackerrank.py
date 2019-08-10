import random

def maxDifference(a):

	diff_list = []
	min_val = 0
	for i in range(len(a)):
		print("Evaluating {}".format(i))
		min_val = a[i]
		for j in range (i):
			if a[j] < a[i] and a[j] < min_val:
				min_val = a[j]
		diff_list.append(a[i] - min_val)

	if len(diff_list) > 0:
		diff_list.sort(reverse=True)
		return diff_list[0]
	return -1

random_nums = random.sample(range(-1000000, 1000000), 200000)
#random_nums = random.sample(range(-1000000, 1000000), 500)
print(maxDifference(random_nums))
