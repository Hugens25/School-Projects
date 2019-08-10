num = 2
total = 0
for i in range(2,1001):
    num *= 2

str = str(num)
print(str)

for a in range(len(str)):
    total += int(str[a])


print(total)
