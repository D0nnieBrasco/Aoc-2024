def find_common(arr,pcs):
    if arr:
        sets = [set(pcs[key]) for key in arr]  # Convert lists to sets
        return set.intersection(*sets)  # Find the intersection
    else: return set()

def part1(pcs,array):
    trios = []
    for i in array:
        x = find_common(i, pcs)
        if x != set():
            for k in x:
                p = i.copy()
                p.append(k)
                if sorted(p) not in trios: trios.append(sorted(p))
    sum = 0
    for i in trios:
        for j in i:
            if j[0] == 't':
                sum += 1
                break
    print(sum)
def part2(pcs,array):
    longest = []
    for i in array:
        tmp = [i]
        flag = True
        while flag:
            for j in tmp:
                tmp2 = []
                x = find_common(j, pcs)
                if x == set():
                    flag = False
                    break
                for k in x:
                    p = j.copy()
                    p.append(k)
                    tmp2.append(p)
                if len(p) > len(longest): longest = p
                tmp = tmp2
        longest = sorted(longest)
    print(','.join(longest))

with open('text23.txt') as file:
    connections = [line.strip() for line in file]

pcs = {}
for i in connections:
    if i[0:2] not in pcs: pcs[i[0:2]] = [i[-2:]]
    else: pcs[i[0:2]].append(i[-2:])
    if i[-2:] not in pcs: pcs[i[-2:]] = [i[0:2]]
    else: pcs[i[-2:]].append(i[0:2])

array = []
for i in connections:
    array.append([i[0:2],i[-2:]])

part1(pcs, array)
part2(pcs, array)
