num_cases = int(input())
results = []

def is_ordered(str):
    for i in range(len(str) - 1):
        if str[i] >= str[i+1]:
            return False
    return True

for i in range(num_cases):
    word = input().strip()
    if is_ordered(word):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)
