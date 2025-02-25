def part1(arr):
    flag = True
    for i in range(len(arr)):
        if arr[i] == ".":
            for j in range(1, len(arr)):
                if arr[-j] != arr[i]:
                    if i < len(arr) - j:
                        arr[i], arr[-j] = arr[-j], arr[i]
                        # print(arr)
                    else:
                        flag = False
                    break
            if not flag: break

    print(sum(i * int(arr[i]) for i in range(len(arr)) if arr[i] != "."))


def part2(arr):
    taken = []
    for i in range(1, len(arr)):
        if arr[-i] not in taken and arr[-i] != ".":
            l = arr.count(arr[-i])
            for j in range(len(arr) - i):
                if arr[j] == ".":
                    flg = True
                    for k in range(1, l):
                        if arr[j + k] != arr[j]: flg = False
                    if flg:
                        for h in range(l):
                            arr[j + h], arr[-i - h] = arr[-i - h], arr[j + h]
                        taken.append(arr[j])
                        i += l
                        break

    print(sum(i * int(arr[i]) for i in range(len(arr)) if arr[i] != "."))


with open('text9.txt') as file:
    string = file.read()

arr = []
tmp = 0
for i in range(len(string)):
    if i % 2 == 0:
        for j in range(int(string[i])):
            arr.append(str(tmp))
        tmp += 1
    else:
        for j in range(int(string[i])):
            arr.append(".")

part1(arr.copy())
part2(arr)
