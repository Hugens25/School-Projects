lines = [line.rstrip('\n') for line in open('traffic.in')]

for line in lines[1:len(lines)]:
    print(line)
