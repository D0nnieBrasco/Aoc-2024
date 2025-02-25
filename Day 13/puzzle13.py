def calc(a, b, c, d, e, f, part):
    x = (((f + ((part - 1) * 10000000000000)) * b) - ((e + ((part - 1) * 10000000000000)) * d)) / ((b * c) - (a * d))
    return x, ((e + ((part - 1) * 10000000000000)) - (x * a)) / b


def engine(array, part):
    sum = 0
    for i in range(len(array)):
        a, b = calc(array[i][0][0], array[i][1][0], array[i][0][1], array[i][1][1], array[i][2][0], array[i][2][1],
                    part)
        if a == int(a) and b == int(b):
            sum += 3 * a + b
    print(int(sum))

with open('text13.txt') as file:
    arr = [l.split() for l in file]

array = []
for i in range(0, len(arr) - 2, 4):
    array.append([[int(arr[i][2][-3:-1]), int(arr[i][3][-2:])], [int(arr[i + 1][2][-3:-1]), int(arr[i + 1][3][-2:])],
                  [int(arr[i + 2][1][2:-1]), int(arr[i + 2][2][2:])]])

#Part1
engine(array, 1)
#Part2
engine(array, 2)
