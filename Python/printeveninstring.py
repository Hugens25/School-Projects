str = 'Print every word in this sentence that has an even number of letters'
for string in str.split():
    if len(string) % 2 == 0:
        print (string)
