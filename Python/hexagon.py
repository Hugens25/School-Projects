num_cases = int(input())
pieces = {}

for case in range(num_cases):
    vals = input().replace(' ', '')
    i = 0
    j = 5
    count = 0
    while j <= len(vals):
        pieces['{}'.format(count)] = vals[i:j+1]
        i += 6
        j += 6
        count += 1
#print(pieces)

for piece in pieces:

    # pieces[piece] = piece[pieces[piece].index('1'):] + piece[:pieces[piece].index('1')]
    # print(pieces[piece])

    pieces[piece] = pieces[piece][pieces[piece].index('1'):]+pieces[piece][:pieces[piece].index('1')]
    print(pieces[piece])
#print(pieces)
