l = [1,1,1,1,2,2,3,3,3,3,4,5]
newl = []
for num in l:
    if num not in newl:
        newl.append(num)

print(newl)
