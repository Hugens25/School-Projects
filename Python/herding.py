f = open('herding.in')
out = open('herding.out', 'w+')
line = f.readline()
locations = list(map(int, line.split()))
output = []
min = 0

locations.sort()

if locations[0] + 1 == locations[1] == locations[2] - 1:
    max = 0
else:
    if locations[1] - locations[0] > locations[2] - locations[1]:
        max = locations[1] - locations[0] - 1
    else:
        max = locations[2] - locations[1] - 1

if locations[0] + 2 == locations[1] or locations[2] - 2 == locations[1]:
    min = 1
elif locations[0] + 1 == locations[1] == locations[2] - 1:
    min = 0
else:
    min = 2

out.write(str(min)+'\n')
out.write(str(max))

f.close()
out.close()
