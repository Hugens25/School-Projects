def gensquare(n):
    for i in range(n):
        yield i**2

print(list(gensquare(5)))
