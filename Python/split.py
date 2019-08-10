str = 'Print only the words that start with s in this sentence'
strlist = str.split()
for string in strlist:
  if string[0] == 's':
    print(string)
