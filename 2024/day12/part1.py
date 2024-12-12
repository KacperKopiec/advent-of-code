import os
from collections import deque

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
flag = [[False for _ in range(len(f[0]))] for _ in range(len(f))]

def in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def neighbors4(grid, row, col):
    for dr, dc in DIRECTIONS:
        rr, cc = row + dr, col + dc
        if in_bounds(grid, rr, cc):
            yield (rr, cc)

ans = 0
for i in range(len(f)):
    for j in range(len(f[0])):
        if not flag[i][j]:
            area, p = 0, 0
            q = deque()
            q.append((i, j))
            while len(q):
                y, x = q.popleft()
                if flag[y][x]: continue
                flag[y][x] = True
                area += 1
                if y == 0 or y == len(f) - 1: p += 1
                if x == 0 or x == len(f[0]) - 1: p += 1

                for a, b in neighbors4(f, y, x):
                    if f[y][x] == f[a][b] and not flag[a][b]: q.append((a, b))
                    elif f[y][x] != f[a][b]: p += 1
            ans += area * p
print(ans)  