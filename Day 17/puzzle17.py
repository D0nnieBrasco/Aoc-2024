def calc(A, B, C, instr):
    pointer = 0
    out = []
    while pointer < len(instr):
        combo = [0, 1, 2, 3, A, B, C]
        opco, oper = instr[pointer], instr[pointer + 1]
        if opco == 0:
            A = A >> combo[oper]
        elif opco == 1:
            B = B ^ oper
        elif opco == 2:
            B = combo[oper] & 7
        elif opco == 3:
            if A != 0:
                pointer = oper
                continue
        elif opco == 4:
            B = B ^ C
        elif opco == 5:
            out.append(combo[oper] & 7)
        elif opco == 6:
            B = A >> combo[oper]
        elif opco == 7:
            C = A >> combo[oper]
        pointer += 2
    return out

def find(a, i, prog):
    if calc(a, 0, 0, prog) == prog:
        print(a)
        exit()
    elif calc(a, 0, 0, prog) == prog[-i:] or not i:
        for n in range(8): find((8 * a) + n, i + 1, prog)

with open('text17.txt') as file:
    lines = file.read().replace("Register", '').replace("A:", '').replace("B:", '').replace("C:", '').replace(
        "Program:", '').split()

A = int(lines[0])
B = int(lines[1])
C = int(lines[2])
instr = list(map(int, lines[3].replace(',', '')))
print(','.join(str(i) for i in calc(A, B, C, instr)))
find(0, 0, instr)
