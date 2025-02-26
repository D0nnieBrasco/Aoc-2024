from collections import deque

def generate_map(n, bytes):
    map = [list(n * '.') for i in range(n)]
    for i in bytes:
        map[int(i[1])][int(i[0])] = '#'
    return map

def bfs(maze):
    queue = deque()
    queue.append((0, 0, 0))
    maze[0][0] = 0
    visited = set()
    while queue:
        y, x, distance = queue.popleft()
        if (y, x) in visited: continue
        visited.add((y, x))
        if (y, x) == (len(maze) - 1, len(maze) - 1):
            return distance
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= y + dir[0] < len(maze) and 0 <= x + dir[1] < len(maze) and maze[y + dir[0]][x + dir[1]] == '.':
                queue.append((y + dir[0], x + dir[1], distance + 1))
                maze[y + dir[0]][x + dir[1]] = distance + 1

with open('text18.txt') as file:
    bytes = [list(l.replace(',', ' ').split()) for l in file]

map = generate_map(71, bytes[:1024])
#Part1
print(bfs(map.copy()))
for i in range(1024, 3000):
    map = generate_map(71, bytes[:i])
    if not bfs(map.copy()):
        #Part2
        print(','.join(bytes[i - 1]))
        break
