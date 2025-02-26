def operation(line,states):
    if line[1] == 'AND': return states[line[0]] and states[line[2]]
    elif line[1] == 'OR': return states[line[0]] or states[line[2]]
    else: return states[line[0]] ^ states[line[2]]

with open('text24.txt') as file:
    array = [l.strip().replace(":","").split() for l in file]

states = {}
for i in array.copy():
    if i and '->' not in i and i[0] not in states:
        states[i[0]] = int(i[1])
    if len(i) < 3: array.pop(0)

flag = True
while flag:
    counter = 0
    for i in array:
        if (i[0] in states) and (i[2] in states) and (i[4] not in states):
            states[i[4]] = operation(i,states)
            counter += 1
    if counter == 0: flag = False

states = {k: states[k] for k in sorted(states)}
score = ""
for k,v in states.items():
    if k[0] == 'z': score += str(v)

#Part1
print(int(score[::-1],2))

find = []
for o1, oper, o2,_, s in array:
    if s[0] == 'z' and oper != 'XOR' and s != "z45":
        find.append(s)
    if oper == "XOR" and \
            s[0] not in ["x", "y", "z"] and \
            o1[0] not in ["x", "y", "z"] and \
            o2[0] not in ["x", "y", "z"]:
        find.append(s)
    if oper == "AND" and "x00" not in [o1, o2]:
        for to1, toper, to2, _, __ in array:
            if (s == to1 or s == to2) and toper != "OR":
                find.append(s)
    if oper == "XOR":
        for t_o1, t_oper, t_o2, _, __ in array:
            if (s == t_o1 or s == t_o2) and t_oper == "OR":
                find.append(s)

#Part2
print(','.join(sorted(set(find))))
