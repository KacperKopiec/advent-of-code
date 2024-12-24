import os
from collections import deque
from math import inf

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
HEIGHT = 71
WIDTH = 71
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def neighbors4(grid, row, col):
    for dr, dc in DIRECTIONS:
        rr, cc = row + dr, col + dc
        if in_bounds(grid, rr, cc) and grid[rr][cc] == '.':
            yield (rr, cc)

def bfs():
    dist = [[inf for _ in range(WIDTH)] for _ in range(HEIGHT)]
    dist[0][0] = 0
    q = deque()
    q.append((0, 0))
    while len(q):
        y, x = q.popleft()
        for i, j in neighbors4(grid, y, x):
            if dist[y][x] + 1 < dist[i][j]:
                dist[i][j] = dist[y][x] + 1
                q.append((i, j))

    return dist[-1][-1] != inf

for line in f:
    x, y = list(map(int, line.split(',')))
    grid[y][x] = '#'
    if not bfs():
        print(f"{x},{y}")
        break