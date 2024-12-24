import os
from collections import deque
from math import inf

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIRECTIONS_CHEAT = [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)] 
def in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def neighbors4(grid, row, col):
    for dr, dc in DIRECTIONS:
        rr, cc = row + dr, col + dc
        if in_bounds(grid, rr, cc) and grid[rr][cc] != '#':
            yield (rr, cc)

def cheat(grid, row, col):
    for dr, dc in DIRECTIONS_CHEAT:
        rr, cc = row + dr, col + dc
        if in_bounds(grid, rr, cc) and grid[rr][cc] != '#':
            yield (rr, cc)

def bfs(source):
    dist = [[inf for _ in range(len(f[0]))] for _ in range(len(f))]
    dist[source[0]][source[1]] = 0
    q = deque()
    q.append(source)
    while len(q):
        y, x = q.popleft()
        for i, j in neighbors4(f, y, x):
            if dist[y][x] + 1 < dist[i][j]:
                dist[i][j] = dist[y][x] + 1
                q.append((i, j))
    return dist

for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == 'S':
            from_start = bfs((i, j))
        if f[i][j] == 'E':
            time = from_start[i][j]
            from_end = bfs((i, j))

ans = 0
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] != '#':
            for a, b in cheat(f, i, j):
                if time - (from_start[i][j] + from_end[a][b] + 2) >= 100:
                    ans += 1
print(ans)