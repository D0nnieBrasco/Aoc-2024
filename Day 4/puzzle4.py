def scan_for_xmas_str(array):
    counter = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "X":
                # horizontal scan ->
                if j + 4 <= len(array[i]):
                    if array[i][j + 1:j + 4] == "MAS": counter += 1

                # horizontal scan <-
                if j > 2:
                    if array[i][j - 3:j] == "SAM": counter += 1

                # vertical up to down
                if i + 4 <= len(array):
                    if array[i + 1][j] == "M" and array[i + 2][j] == "A" and array[i + 3][j] == "S": counter += 1

                # vertical down to up
                if i > 2:
                    if array[i - 1][j] == "M" and array[i - 2][j] == "A" and array[i - 3][j] == "S": counter += 1

                # to north east
                if i > 2 and j + 4 <= len(array[i]):
                    if array[i - 1][j + 1] == "M" and array[i - 2][j + 2] == "A" and array[i - 3][
                        j + 3] == "S": counter += 1

                # to north west
                if i > 2 and j > 2:
                    if array[i - 1][j - 1] == "M" and array[i - 2][j - 2] == "A" and array[i - 3][
                        j - 3] == "S": counter += 1

                # to south east
                if i + 4 <= len(array) and j + 4 <= len(array[i]):
                    if array[i + 1][j + 1] == "M" and array[i + 2][j + 2] == "A" and array[i + 3][
                        j + 3] == "S": counter += 1

                # to south west
                if i + 4 <= len(array) and j > 2:
                    if array[i + 1][j - 1] == "M" and array[i + 2][j - 2] == "A" and array[i + 3][
                        j - 3] == "S": counter += 1
    return counter


def scan_for_mas_str(array):
    counter = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "A" and 0 < i < len(array) - 1 and 0 < j < len(array[i]) - 1:

                # M up
                if array[i - 1][j - 1] == "M" and array[i - 1][j + 1] == "M" and array[i + 1][j - 1] == "S" and \
                        array[i + 1][j + 1] == "S": counter += 1

                # M down
                if array[i - 1][j - 1] == "S" and array[i - 1][j + 1] == "S" and array[i + 1][j - 1] == "M" and \
                        array[i + 1][j + 1] == "M": counter += 1

                # M left
                if array[i - 1][j - 1] == "M" and array[i - 1][j + 1] == "S" and array[i + 1][j - 1] == "M" and \
                        array[i + 1][j + 1] == "S": counter += 1

                # M right
                if array[i - 1][j - 1] == "S" and array[i - 1][j + 1] == "M" and array[i + 1][j - 1] == "S" and \
                        array[i + 1][j + 1] == "M": counter += 1

    return counter

with open('text4.txt') as file:
    arr = [l for l in file]

print(scan_for_xmas_str(arr)) #part1
print(scan_for_mas_str(arr)) #part2
