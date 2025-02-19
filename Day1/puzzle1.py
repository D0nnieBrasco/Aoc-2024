part1 = lambda a1, a2:  print(sum(abs(a1[i] - a2[i]) for i in range(len(a1))))
part2 = lambda a1, a2: print(sum(i * a2.count(i) for i in a1))

with open('text1.txt') as file:
    arr = [l.split() for l in file]

id_1, id_2 = [], []

for i in arr:
    id_1.append(int(i[0]))
    id_2.append(int(i[1]))

id_1.sort()
id_2.sort()

part1(id_1,id_2)
part2(id_1,id_2)
