def verify_update(order, dictionary):
    for j in range(len(order)):
        for k in range(len(order) - j - 1):
            if not order[j + k + 1] in dictionary[order[j]]:
                return False
    return True

def find_positions(order, dictionary):
    tmp = ['' for i in order]
    for i in range(len(order)):
        counter = 0
        for j in range(len(order)):
            if i!= j:
                if order[i] in dictionary[order[j]]: counter += 1
        tmp[counter] = order[i]
    return int(tmp[len(order)//2])

with open('text5.txt') as file:
    lines = file.readlines()

rules = [line.strip().replace('|', ' ').split() for line in lines if '|' in line]
order = [line.strip().replace(',', ' ').split() for line in lines if ',' in line]

rules_left = [i[0] for i in rules]
rules_right = [i[1] for i in rules]

book = {}

for i in range(len(rules_left)):
    if rules_left[i] not in book: book[rules_left[i]] = [rules_right[i]]
    else: book[rules_left[i]].append(rules_right[i])

arr_of_wrong = []

counter = 0
for i in order:
    if verify_update(i,book): counter += int(i[int((len(i)-1)/2)])
    else: arr_of_wrong.append(i)

#Part1
print(counter)
#Part2
print(sum(find_positions(i,book) for i in arr_of_wrong))
