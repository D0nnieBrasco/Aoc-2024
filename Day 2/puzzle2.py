def check(x):
    if len(x) == len(set(x)):
        j = x.copy()
        k = x.copy()
        j.sort()
        k.sort(reverse=True)
        if x == j or x == k:
            counter = 0
            for p in range(len(x)):
                if p > 0:
                    if abs(x[p] - x[p-1]) > counter: counter = abs(x[p] - x[p-1])
            if counter < 4:
                return True

with open('text2.txt') as file:
    arr = [l.split() for l in file]

part1 = part2 = 0

for x in range(len(arr)):
    for j in range(len(arr[x])):
        arr[x][j] = int(arr[x][j])

    if check(arr[x]):
        part1 += 1
        part2 += 1
    else:
        for j in range(len(arr[x])):
            cop = arr[x].copy()
            del cop[j]
            if check(cop):
                part2 += 1
                break

print(part1)
print(part2)
