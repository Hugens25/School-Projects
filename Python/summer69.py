l = [2,1,6,9,11]
canAdd = True
sum = 0

for element in l:
    if element == 6 and canAdd == True:
        canAdd = False
    elif element == 9 and canAdd == False:
        canAdd = True
    elif canAdd == True:
        sum += element

print (sum)
