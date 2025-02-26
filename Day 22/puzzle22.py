def next_secret(x):
    x = x^(x << 6) % 16777216
    x = x^(x >> 5) % 16777216
    x = x^(x << 11) % 16777216
    return x

def part1(secrets):
    sum = 0
    for i in secrets.copy():
        for j in range(2000):
            i = next_secret(i)
        sum += i
    print(sum)

def part2(secrets):
    dic = {}
    diffs = []
    mirror = []
    for i in secrets.copy():
        tmp = {}
        for j in range(2000):
            x = i
            i = next_secret(i)
            diffs.append(i % 10 - x % 10)
            if j > 2:
                if (diffs[-4], diffs[-3], diffs[-2], diffs[-1]) not in dic: dic[
                    (diffs[-4], diffs[-3], diffs[-2], diffs[-1])] = 0
                if (diffs[-4], diffs[-3], diffs[-2], diffs[-1]) not in tmp:  tmp[
                    (diffs[-4], diffs[-3], diffs[-2], diffs[-1])] = i % 10
        mirror.append(tmp)

    for k in dic:
        for i in mirror:
            if k in i:
                dic[k] += i[k]

    dic = {k: v for k, v in sorted(dic.items(), key=lambda i: i[1], reverse=True)}  # sorting
    print(list(dic.items())[0][1])

with open('text22.txt') as file:
    secrets  = [int(line) for line in file]

part1(secrets.copy())
part2(secrets.copy())
