part1 = lambda arr1, arr2:  print(sum(abs(arr1[i] - arr2[i]) for i in range(len(arr1))))
part2 = lambda arr1, arr2: print(sum(i * arr2.count(i) for i in arr1))

with open('text1.txt') as file:
    arr = [l.split() for l in file]

arr_id_1, arr_id_2 = [], []

for i in arr:
    arr_id_1.append(int(i[0]))
    arr_id_2.append(int(i[1]))

arr_id_1.sort()
arr_id_2.sort()

part1(arr_id_1,arr_id_2)
part2(arr_id_1,arr_id_2)
