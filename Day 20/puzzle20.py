from collections import deque

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] in ('S', 'E'):
                if maze[i][j] == 'S': return (i,j) #start y,x

def bfs(maze,start):
    queue = deque()
    queue.append((start[0],start[1],0)) # Y, X, Steps from start
    maze[start[0]][start[1]] = 0
    visited = set()
    while queue:
        y, x, distance = queue.popleft()
        if (y, x) in visited: continue
        visited.add((y, x))
        for dir in [(1,0),(0,1),(-1,0),(0,-1)]:
            if maze[y + dir[0]][x + dir[1]] in ('.','E'):
                queue.append((y + dir[0], x + dir[1], distance + 1))
                maze[y + dir[0]][x + dir[1]] = distance + 1
    return visited

def solve(maze, visited, cheat_time, save):
    correct_cheats = 0
    possible_cheats = generate(cheat_time)
    for v in visited:
        for i in possible_cheats:
            if 1 <= v[0]+i[0] < len(maze)-1 and 1 <= v[1]+i[1] < len(maze[v[0]])-1:
                if isinstance(maze[v[0]+i[0]][v[1]+i[1]], int):
                    if maze[v[0]+i[0]][v[1]+i[1]] - maze[v[0]][v[1]] >= save+(abs(i[0])+abs(i[1])):
                        correct_cheats += 1
    print(correct_cheats)

def generate(steps):
    visited = set()
    visited.add((0,0))
    for i in range(steps):
        for v in visited.copy():
            for d in [(1,0),(-1,0),(0,-1),(0,1)]:
                visited.add((v[0]+d[0],v[1]+d[1]))
    visited.remove((0,0))
    for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        visited.remove(d)
    return visited

with open('text20.txt') as file:
    maze = [list(l.strip()) for l in file]

S = find_start(maze)
visited = bfs(maze,S)
solve(maze,visited,2,100)
solve(maze,visited,20,100)
