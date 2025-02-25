def check_further(map, i, j, paths, paths2, ii, jj):
    if int(map[i][j]) == 9:
        if [(ii, jj), (i, j)] not in paths: paths.append([(ii, jj), (i, j)])
        # paths to part2
        paths2.append(1)
    a = str(int(map[i][j]) + 1)  # looking for next number

    # right
    if j + 1 < len(map[i]):
        if map[i][j + 1] == a: check_further(map, i, j + 1, paths, paths2, ii, jj)
    # left
    if j > 0:
        if map[i][j - 1] == a: check_further(map, i, j - 1, paths, paths2, ii, jj)
    # up
    if i > 0:
        if map[i - 1][j] == a: check_further(map, i - 1, j, paths, paths2, ii, jj)
    # down
    if i + 1 < len(map):
        if map[i + 1][j] == a: check_further(map, i + 1, j, paths, paths2, ii, jj)


with open('text10_24.txt') as file:
    map = [l for l in file]

paths = []
paths2 = []

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "0":
            check_further(map, i, j, paths, paths2, i, j)  # map,pos of 0, arrays to sum, pos of 0 to not make duplicates

print(len(paths))
print(sum(paths2))
