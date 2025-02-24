def check_if_possible(substrats, score, part2=None):
    results = []
    a = 3 if part2 else 2
    for i in range(len(substrats)):
        if i == 0:
            results.append(int(substrats[0]))
        if i == 1:
            results.append(results[0] + int(substrats[1]))
            results.append(results[0] * int(substrats[1]))
            if part2: results.append(int(str(results[0]) + substrats[1]))
        else:
            for j in range(int(a ** (i - 1))):  # add
                results.append(results[-1 - (2 * j)] + int(substrats[i]))
            for j in range(int(a ** (i - 1))):  # multiply
                results.append(results[-1 - (a ** (i - 1)) - (2 * j)] * int(substrats[i]))
            if part2:
                for j in range(int(3 ** (i - 1))):  # assemble
                    results.append(int(str(results[-1 - (2 * (a ** (i - 1))) - (2 * j)]) + substrats[i]))

    return True if score in results[-1 * (a ** (len(substrats) - 1)):] else False


with open('text7.txt') as file:
    text = [l.replace(":", " ").split() for l in file]

scores = [int(i[0]) for i in text]
substrats = [i[1:] for i in text]

# Part1
print(sum(scores[i] for i in range(len(scores)) if check_if_possible(substrats[i], scores[i])))
# Part2
print(sum(scores[i] for i in range(len(scores)) if check_if_possible(substrats[i], scores[i], True)))
