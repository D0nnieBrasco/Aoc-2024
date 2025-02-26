def f(towels,design, ways, way): 
    if not design:
        return True
    for i in towels:
        l = len(i)
        if l <= len(design):
            if design[:l] == i:
                if way + design[:l] not in ways:
                    tmp = way + i
                    ways.append(tmp)
                    if f(towels,design[l:], ways, tmp): return True

def f2(towels,design):
    tmp = {}
    longest = 0
    score = 0
    for i in towels:
        if len(i) > longest: longest = len(i)
        if design[:len(i)] == i: tmp[i] = 1

    while tmp:
        copy = tmp.copy()
        tmp = {}
        for i in copy:
            l = len(i)
            for j in range(1,longest+1):
                if design[l:l+j] in towels:
                    if len(i)+ j <= len(design):
                        if i+design[l:l+j] not in tmp:
                            tmp[i+design[l:l+j]] = copy[i]
                        else:
                            tmp[i+design[l:l+j]] += copy[i]
        if design in tmp:
            score += tmp[design]
            del tmp[design]
        if not tmp:break

    return score

with open('text19_24.txt') as file:
    array = [l.strip() for l in file]
towels = array[0].replace(',','').split()
designs = array[2:]

#Part1
print(sum(1 for i in designs if f(towels, i, [],"")))
#Part2
print(sum(f2(towels, i) for i in designs))
