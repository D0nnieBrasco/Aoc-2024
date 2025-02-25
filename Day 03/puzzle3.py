import re

def strings_to_integers_and_multiply(str):
    l1 = l2 = ""
    for i in range(len(str)):
        if str[i] != ",":
            l1 = l1 + str[i]
        else:
            l2 += str[i + 1:]
            break
    return int(l1) * int(l2)

with open('text3.txt') as file:
    arr = [l for l in file]

pattern = r"mul\(\d+,\d+\)"
tmp = "".join(arr)
mularr = re.findall(pattern, tmp)

print(sum(strings_to_integers_and_multiply(i[4:-1]) for i in mularr))

# part2
tmp2 = ""
flag = True
for i in range(len(tmp)):
    if len(tmp) > i + 6:
        if tmp[i:i + 7] == "don't()": flag = False
        elif tmp[i:i + 4] == "do()": flag = True
    if flag: tmp2 = tmp2 + tmp[i]

mularr2 = re.findall(pattern, tmp2)

print(sum(strings_to_integers_and_multiply(i[4:-1]) for i in mularr2))
