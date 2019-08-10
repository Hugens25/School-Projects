def palindrome(str):
    s = ''
    newstr = s.join(str.split())
    return newstr[::1] == newstr[::-1]

print(palindrome('nurses run'))
