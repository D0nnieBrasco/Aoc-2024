def blink(dic,blinks):
    for b in range(blinks):
        copp = dic.copy()
        for i in dic.copy():
            if i == 0:
                if 1 not in dic:
                    dic[1] = copp[i]
                else:
                    dic[1] += copp[i]
            elif len(str(i))%2 == 0:
                tmp = str(i)
                if int(tmp[:int(len(tmp)/2)]) not in dic:
                    dic[int(tmp[:int(len(tmp)/2)])] = copp[i]
                else:
                    dic[int(tmp[:int(len(tmp)/2)])] += copp[i]

                if int(tmp[int(len(tmp)/2):]) not in dic:
                    dic[int(tmp[int(len(tmp)/2):])] = copp[i]
                else:
                    dic[int(tmp[int(len(tmp)/2):])] += copp[i]
            else:
                if i*2024 not in dic:
                    dic[i*2024] = copp[i]
                else:
                    dic[i*2024] += copp[i]
        for i in copp:
            if dic[i] - copp[i] == 0: del dic[i]
            else: dic[i] -= copp[i]

with open('text11.txt') as file:
    stones = [int(i) for i in file.readline().split()]

dic = {}
for i in stones:
    if i not in dic: dic[i] = 1
    else: dic[i] += 1

# Part1
blink(dic, 25)
print(sum(dic[i] for i in dic))

# Part2
blink(dic, 50)
print(sum(dic[i] for i in dic))
