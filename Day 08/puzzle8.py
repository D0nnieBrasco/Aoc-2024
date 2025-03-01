def find_yx_of_antinodes(a1,a2,h,l,antinodes,part2=None):
    vector = (a1[0]-a2[0],a1[1]-a2[1])
    anti1 = (a1[0] + vector[0],a1[1] + vector[1])
    anti2 = (a2[0] - vector[0],a2[1] - vector[1])

    if 0 <= anti1[0] < h and 0 <= anti1[1] < l and anti1 not in antinodes: antinodes.append(anti1)
    if 0 <= anti2[0] < h and 0 <= anti2[1] < l and anti2 not in antinodes: antinodes.append(anti2)

    if part2:
        if a1 not in antinodes: antinodes.append(a1)
        if a2 not in antinodes: antinodes.append(a2)

    while part2:
        end_loop = 0
        anti1 = (anti1[0] + vector[0], anti1[1] + vector[1])
        anti2 = (anti2[0] - vector[0], anti2[1] - vector[1])
        if 0 <= anti1[0] < h and 0 <= anti1[1] < l:
            if anti1 not in antinodes: antinodes.append(anti1)
        else:
            end_loop += 1
        if 0 <= anti2[0] < h and 0 <= anti2[1] < l:
            if anti2 not in antinodes: antinodes.append(anti2)
        else:
            end_loop += 1
        if end_loop == 2: break

def find_antinodes(h,l,antennas,antinodes,part2=None):
    for i in range(len(antennas)-1):
        for j in range(1+i,len(antennas)):
            find_yx_of_antinodes(antennas[i], antennas[j], h, l, antinodes, part2)

with open('text8.txt') as file:
    map = [list(l.strip()) for l in file]

characters = {}
antinodes1, antinodes2 = [], []
#scanning for different characters through map
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != ".":
            if map[i][j] not in characters: characters[map[i][j]] = [(int(i),int(j))]
            else: characters[map[i][j]].append((int(i),int(j)))

h = len(map)
l = len(map[0])
for k,v in characters.items():
    find_antinodes(h, l, v, antinodes1)
    find_antinodes(h, l, v, antinodes2,True)

#Part1
print(len(antinodes1))
#Part2
print(len(antinodes2))
