def main_keyboard(start,stop,dic):
    if stop == 'A':
        return dic[start][10] + 'A'
    else:
        return dic[start][int(stop)] + 'A'

def steering_keyboard(line,dic,dic2,dic3,depth):
    start_state = 'A'
    tmp = 0
    for i in line:
        tmp += robot_keyboard(start_state,i,dic,dic2,dic3,depth)
        start_state = i
    return tmp

def robot_keyboard(start,stop,dic,dic2,dic3,depth):
    tmp = main_keyboard(start,stop,dic)
    state = 'A'
    dic3 = {k: 0 for k in dic3}
    for i in range(len(tmp)):
        dic3[state+tmp[i]] += 1
        state = tmp[i]

    for i in range(depth):
        dic4 = dic3.copy()
        dic3 = {k: 0 for k in dic3}
        for k, v in dic4.items():
            if v > 0:
                ty = k
                ty2 = dic2[ty[0]][dic2[ty[1]][5]]
                state = 'A'
                for m in range(len(ty2)):
                    dic3[state+ty2[m]] += v
                    state = ty2[m]
        sum = 0
        for k,v in dic3.items(): sum += v
    return sum

def count(n):
    for j in range(2, n):
        sum = 0
        for i in lines:
            x = steering_keyboard(i, dic, dic2, dic3, j)
            sum += x * int(i[:-1])
    #print(f"Depth = {j + 1}\nTime = {time.time() - t1}\nSum of the complexities = {sum}\n")
    print(sum)

with open('text21.txt') as file:
    lines = [line.strip() for line in file]

dic = {
    'A': ('<','^<<','<^','^','^^<<','^^<','^^','^^^<<','<^^^','^^^',''), #0123456789A
    '0': ('','^<','^','^>','^^<','^^','^^>','^^^<','^^^','^^^>','>'),
    '1': ('>v','','>','>>','^','^>','^>>','^^','^^>','^^>>','^^v'),
    '2': ('v','<','','>','^<','^','^>','^^<','^^','^^>','>v'),
    '3': ('v<','<<','<','','^<<','^<','^','<<^^','^^<','^^','v'),
    '4': ('>vv','v','>v','>>v','','>','>>','^','^>','^>>','>>vv'),
    '5': ('vv','v<','v','>v','<','','>','^<','^','^>','vv>'),
    '6': ('vv<','<<v','<v','v','<<','<','','<<^','^<','^','vv'),
    '7': ('>vvv','vv','vv>','>>vv','v','v>','v>>','','>','>>','>>vvv'),
    '8': ('vvv','vv<','vv','vv>','<v','v','>v','<','','>','>vvv'),
    '9': ('<vvv','vv<<','vv<','vv','v<<','v<','v','<<','<','','vvv'),
}

dic2 = {
    'A': ('<A','vA','<vA','v<<A','A',4), # ^>v<Aself
    '<': ('>^A','>>A','>A','A','>>^A',3),
    'v': ('^A','>A','A','<A','^>A',2),
    '^': ('A','v>A','vA','v<A','>A',0),
    '>': ('<^A','A','<A','<<A','^A',1)
}

dic3 = {
    'AA': 0,
    'A^': 0,
    'A>': 0,
    'Av': 0,
    'A<': 0,
    '^A': 0,
    '^^': 0,
    '^>': 0,
    '^v': 0,
    '^<': 0,
    '>A': 0,
    '>^': 0,
    '>>': 0,
    '>v': 0,
    '><': 0,
    'vA': 0,
    'v^': 0,
    'v>': 0,
    'vv': 0,
    'v<': 0,
    '<A': 0,
    '<^': 0,
    '<>': 0,
    '<v': 0,
    '<<': 0,
}

count(3) #Part1
count(26) #Part2
