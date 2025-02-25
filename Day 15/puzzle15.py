def move_blocks(arr,blocks,dir,p):
    for i in blocks:
        swap_vertical(arr, i[0][0] + dir[0], i[0][1], i[0][0])
        swap_vertical(arr, i[1][0] + dir[0], i[1][1], i[1][0])

    swap_vertical(arr,p[0] + dir[0],p[1], p[0])

def check_blocks(arr,y,x,diry,blocks):
    tmp = []
    if arr[y][x] =='[': tmp = [(y,x),(y,x+1)]
    elif arr[y][x] ==']': tmp = [(y,x),(y,x-1)]
    move = True
    for i in tmp:
        if arr[i[0]+diry][i[1]] == '#': return False
        if arr[i[0]+diry][i[1]] in ('[',']'):
            move = check_blocks(arr,i[0]+diry,i[1],diry,blocks)
            if not move: break
    if move:
        if tmp not in blocks and [tmp[1],tmp[0]] not in blocks: blocks.append(tmp)
        return True
    else:
        return False

def modify_map2(arr, p, dir):
    y, tmpy, x, tmpx = p[0], p[0], p[1], p[1]
    if arr[y + dir[0]][x + dir[1]] != "#":
        counter = 0
        blocks = []
        while arr[tmpy + dir[0]][tmpx + dir[1]] in ('[',']','O'):
            counter += 1
            tmpy += dir[0]
            tmpx += dir[1]
            if dir[2] == 'v' and arr[tmpy][tmpx] in ('[',']'):
                if check_blocks(arr,tmpy,tmpx,dir[0],blocks):
                    move_blocks(arr,blocks,dir,p)
                    p[0] += dir[0]
                    p[1] += dir[1]
                break

        if dir[2] == 'h' or (dir[2] == 'v' and counter == 0) or (dir[2] == 'v' and arr[tmpy][tmpx] == 'O'):
            last = arr[tmpy + dir[0]][tmpx + dir[1]]
            counter += 1
            tmpy += dir[0]
            tmpx += dir[1]
            if last == ".":
                for i in range(counter):
                    if dir[2] == 'h':
                        swap_horizontal(arr, y, tmpx + (dir[1]*-1)*(1 + i), tmpx + (dir[1]*-1)*i)
                    elif dir[2] == 'v':
                        swap_vertical(arr, tmpy + (dir[0] * -1) * i, x, tmpy + (dir[0] * -1) * (1 + i))
                p[0] += dir[0]
                p[1] += dir[1]


def swap_horizontal(arr,y,x,x2):
    if x2 > x: x,x2 = x2,x
    arr[y] = arr[y][:x2] + arr[y][x] + arr[y][x2] + arr[y][x+1:]

def swap_vertical(arr,y,x,y2):
    tmp = arr[y][x]
    arr[y] = arr[y][:x] + arr[y2][x] + arr[y][x+1:]
    arr[y2] = arr[y2][:x] + tmp + arr[y2][x+1:]

def sum_map(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in ('O','['): sum += i*100+j
    print(sum)

def find_player(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@": return [i, j]

def extend_map(map):
    tmpmap = []
    for i in map:
        tmp = ''
        for j in i:
            if j == '#':tmp += '##'
            elif j == 'O':tmp += '[]'
            elif j == '.':tmp += '..'
            else:tmp += '@.'
        tmpmap.append(tmp)
    return tmpmap

def part(map,path,player,dir):
    for m in path:
        modify_map2(map, player, dir[m])
    sum_map(map)

with open('text15.txt') as file:
    map = [l[:-1].strip() for l in file]

directions = {
    '>': (0,1,'h'),
    '<': (0,-1,'h'),
    '^': (-1,0,'v'),
    'v': (1,0,'v')
}

path = map[-1]
map.pop()
map2 = extend_map(map)

player = find_player(map)
player2 = find_player(map2)

#Part1
part(map,path,player,directions) #1526673
#Part2
part(map2,path,player2,directions) #1535509
