def check_fiting(lock,key):
    counter = 0
    for i in range(len(lock[0])): #counting how many 'i' elements == #
        for j in range(len(lock)):
            if lock[j][i] == '#': counter += 1
            if key[j][i] == '#': counter += 1
        if counter > 7: return False
        counter = 0
    return True

with open('text25.txt') as file:
    lines = file.read().strip().split()

locks, keys, tmparr = {}, [], []

for i in range(len(lines)):
    tmparr.append(lines[i])
    if (i+1)%7 == 0:
        if tmparr[0] == '.....': keys.append(tmparr)
        else: locks[tuple(tmparr)] = []
        tmparr = []

for k,v in locks.items():
    for i in keys:
        if check_fiting(k,i): locks[k].append(i)

print(sum(len(v) for v in locks.values()))
