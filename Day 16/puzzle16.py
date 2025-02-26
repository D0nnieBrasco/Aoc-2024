from collections import deque

def find_SE(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] in ('S', 'E'):
                if maze[i][j] == 'S':
                    start = (i, j)  
                else:
                    end = (i, j)  
    return start, end

def turn_right(d):
    if d[1] == 0:
        return d[1] * -1, d[0] * -1
    else:
        return d[1] * 1, d[0] * 1

def turn_left(d):
    if d[1] == 0:
        return d[1] * 1, d[0] * 1
    else:
        return d[1] * -1, d[0] * -1

def bfs(maze, S, E):
    queue = deque()
    start = (S[0], S[1], (0, 1), 0)  # start YX, direction, score
    queue.append(start)

    while queue:
        current = queue.popleft()
        cur_y, cur_x = current[0], current[1]
        cur_dir = current[2]
        cur_score = current[3]

        directions = [
            (cur_dir, cur_score + 1),
            (turn_left(cur_dir), cur_score + 1001),
            (turn_right(cur_dir), cur_score + 1001)
        ]

        for new_dir, new_score in directions:
            new_y, new_x = cur_y + new_dir[0], cur_x + new_dir[1]
            if maze[new_y][new_x] == "#":
                continue

            elif maze[new_y][new_x] in (".", "E") or (
                    isinstance(maze[new_y][new_x], int) and maze[new_y][new_x] > new_score):
                maze[new_y][new_x] = new_score
                queue.append((new_y, new_x, new_dir, new_score))

    return maze[E[0]][E[1]]

def best_paths_tiles(maze, S, E, tiles):
    y, x = E
    ly, lx = E  # something random at start for hardcore case
    while (y, x) != S:
        y1, x1 = 0, 0
        for i in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if maze[y + i[0]][x + i[1]] != '#':
                if maze[y + i[0]][x + i[1]] == 'S':
                    y1, x1 = y + i[0], x + i[1]
                    tiles.append((y1, x1))
                    break
                elif maze[y][x] - maze[y + i[0]][x + i[1]] == 1 or maze[y][x] - maze[y + i[0]][x + i[1]] == 1001:
                    y1, x1 = y + i[0], x + i[1]
                    tiles.append((y1, x1))
                if maze[y][x] - maze[y + i[0]][x + i[1]] == -999 and maze[ly][lx] - maze[y + i[0]][x + i[1]] == 2:
                    tiles.append((y + i[0], x + i[1]))
                    best_paths_tiles(maze, S, (y + i[0], x + i[1]), tiles)
        ly, lx = y, x  # copy last pos
        y, x = y1, x1  # next position of y, x

with open('text16.txt') as file:
    maze = [list(l.strip()) for l in file]

S, E = find_SE(maze)
print(bfs(maze, S, E))
tiles = [E]
best_paths_tiles(maze, S, E, tiles)
print(len(set(tiles)))
