def find_exit(arr,positions,x,y,states):
    cur_state = ['^', '>', 'v', '<']
    counter = 0
    state = cur_state[counter]
    while x <= len(arr[0]) or y <= len(arr):
        if arr[y + states[state][0]][x + states[state][1]] != "#":
            positions.append((y,x))
            y += states[state][0]  # position update
            x += states[state][1]
        else:
            counter = (counter + 1)%4
            state = cur_state[counter]
        if x in [len(arr[0]) - 1,0] or y in [len(arr) - 1,0]:
            positions.append((y,x))
            return True
    return False

def find_loop(arr,x,y,states):
    positions_state = []
    cur_state = ['^','>','v','<']
    counter = 0
    state = cur_state[counter]
    while x <= len(arr[0]) or y <= len(arr):
        if arr[y + states[state][0]][x + states[state][1]] != "#":
            if [y,x,counter] in positions_state: return False
            positions_state.append([y,x,counter])
            y += states[state][0]  # position update
            x += states[state][1]
        else:
            counter = (counter + 1)%4
            state = cur_state[counter]
        if x in [len(arr[0]) - 1,0] or y in [len(arr) - 1,0]: return True
    return False

with open('text6.txt') as file:
    arr = [list(l[:-1]) for l in file]

x = y = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] in ['^','v','>','<']:
            x, y = j, i

positions = []
states = {
    '^': (-1,0),
    'v': (1,0),
    '>': (0,1),
    '<': (0,-1)
}
#Part1
find_exit(arr, positions, x, y, states)
uniq_positions = []
for i in positions:
    if i not in uniq_positions: uniq_positions.append(i)
print(len(uniq_positions))

#Part2
sum = 0
for i in range(len(uniq_positions)):
    arr[uniq_positions[i][0]][uniq_positions[i][1]] = '#'
    if find_loop(arr, x, y, states): sum += 1
    arr[uniq_positions[i][0]][uniq_positions[i][1]] = '.'
print(len(uniq_positions)-sum)
