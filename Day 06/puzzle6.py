def search(arr,positions,x,y,states,condition=None):
    positions_state = []
    cur_state = ['^','>','v','<']
    counter = 0
    state = cur_state[counter]
    while x <= len(arr[0]) or y <= len(arr):
        if arr[y + states[state][0]][x + states[state][1]] != "#":
            if not condition: positions.append((y,x))
            if [y,x,counter] in positions_state and condition:
                return False
            positions_state.append([y,x,counter])
            y += states[state][0]  # position update
            x += states[state][1]
        else:
            counter = (counter + 1)%4
            state = cur_state[counter]

        if x in [len(arr[0]) - 1,0] or y in [len(arr) - 1,0]:
            if not condition: positions.append((y,x))
            return True
    return False

def modify_map(arr,position,char):
    arr[position[0]][position[1]] = char

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
search(arr, positions, x, y, states)
uniq_positions = []
for i in positions:
    if i not in uniq_positions: uniq_positions.append(i)
print(len(uniq_positions))

#Part2
sum = 0
for i in range(len(uniq_positions)):
    modify_map(arr,uniq_positions[i],"#")
    if search(arr,[], x, y, states, True): sum += 1
    modify_map(arr,uniq_positions[i],".")

print(len(uniq_positions)-sum)
