num_vals = int(input())

all_vals = input().split()
all_vals_rev = all_vals[::-1]

max_vals = []
beg = 0

for i in range(1,len(all_vals)):
    if all_vals[0] != all_vals[i]:
        beg = i

for j in range(len(all_vals)-1, -1, -1):
    if all_vals[len(all_vals)-1] != all_vals[j]:
        end = len(all_vals) - j - 1
print(max(beg, end))
