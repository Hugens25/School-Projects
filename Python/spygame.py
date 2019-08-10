l = [1,0,0,1,3,4,5,6,7,7]
first_zero = False
second_zero = False
seven = False

for num in l:
    if num == 0 and first_zero == False:
        first_zero = True
    elif num == 0 and second_zero == False:
        second_zero = True
    elif num == 7 and first_zero == True and second_zero == True and seven == False:
        seven = True

print(first_zero and second_zero and seven)
