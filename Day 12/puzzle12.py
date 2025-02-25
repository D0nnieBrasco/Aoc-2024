def finder(arr, i, j, cords, pack, pointer):
    sum = 0
    if j > 0:
        if arr[i][j - 1] == arr[i][j]:
            if [i, j - 1] not in cords:
                pack[pointer][1] += 1
                pack[pointer].append([i, j - 1])
                cords.append([i, j - 1])
                finder(arr, i, j - 1, cords, pack, pointer)
            sum += 1
    if j < len(arr[i]) - 1:
        if arr[i][j + 1] == arr[i][j]:
            if [i, j + 1] not in cords:
                pack[pointer][1] += 1
                pack[pointer].append([i, j + 1])
                cords.append([i, j + 1])
                finder(arr, i, j + 1, cords, pack, pointer)
            sum += 1
    if i > 0:
        if arr[i - 1][j] == arr[i][j]:
            if [i - 1, j] not in cords:
                pack[pointer][1] += 1
                pack[pointer].append([i - 1, j])
                cords.append([i - 1, j])
                finder(arr, i - 1, j, cords, pack, pointer)
            sum += 1
    if i < len(arr) - 1:
        if arr[i + 1][j] == arr[i][j]:
            if [i + 1, j] not in cords:
                pack[pointer][1] += 1
                pack[pointer].append([i + 1, j])
                cords.append([i + 1, j])
                finder(arr, i + 1, j, cords, pack, pointer)
            sum += 1
    pack[pointer][2] += abs(sum - 4)


def analyze(i, pack, point):
    arr = i[3:]
    sides = 0

    # up
    up = []
    up_pairs = 0
    for i in range(len(arr)):
        pom = arr[i][0]
        if [pom - 1, arr[i][1]] not in arr:
            up.append(arr[i])
    for i in range(len(up) - 1):
        for j in range(len(up) - i - 1):
            if abs(up[i][1] - up[i + j + 1][1]) == 1 and up[i][0] == up[i + j + 1][0]: up_pairs += 1
    up_sides = len(up) - up_pairs

    # down
    down = []
    down_pairs = 0
    for i in range(len(arr)):
        pom = arr[i][0]
        if [pom + 1, arr[i][1]] not in arr:
            down.append(arr[i])
    for i in range(len(down) - 1):
        for j in range(len(down) - i - 1):
            if abs(down[i][1] - down[i + j + 1][1]) == 1 and down[i][0] == down[i + j + 1][0]: down_pairs += 1
    down_sides = len(down) - down_pairs

    # left
    left = []
    left_pairs = 0
    for i in range(len(arr)):
        pom = arr[i][1]
        if [arr[i][0], pom - 1] not in arr:
            left.append(arr[i])
    for i in range(len(left) - 1):
        for j in range(len(left) - i - 1):
            if abs(left[i][0] - left[i + j + 1][0]) == 1 and left[i][1] == left[i + j + 1][1]: left_pairs += 1
    left_sides = len(left) - left_pairs

    # right
    right = []
    right_pairs = 0
    for i in range(len(arr)):
        pom = arr[i][1]
        if [arr[i][0], pom + 1] not in arr:
            right.append(arr[i])
    for i in range(len(right) - 1):
        for j in range(len(right) - i - 1):
            if abs(right[i][0] - right[i + j + 1][0]) == 1 and right[i][1] == right[i + j + 1][1]: right_pairs += 1
    right_sides = len(right) - right_pairs
    pack[point].append(up_sides + down_sides + left_sides + right_sides)


with open('text12.txt') as file:
    mapp = [l[:-1] for l in file]

cords = []
pack = []
pointer = 0
for i in range(len(mapp)):
    for j in range(len(mapp[i])):
        if [i, j] not in cords:
            cords.append([i, j])
            pack.append([mapp[i][j], 1, 0, [i, j]])
            finder(mapp, i, j, cords, pack, pointer)
            pointer += 1

for i in range(len(pack)): analyze(pack[i], pack, i)

# Part1
print(sum(i[1] * i[2] for i in pack))
# Part2
print(sum(i[1] * i[-1] for i in pack))
