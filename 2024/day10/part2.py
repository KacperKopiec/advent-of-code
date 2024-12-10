import os
from collections import deque

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = list(map(lambda x: list(map(int, list(x))), file.read().strip().split('\n')))

    
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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
        if f[i][j] == 0:
            q = deque()
            q.append((i, j))
            while len(q):
                y, x = q.popleft()
                if f[y][x] == 9:
                    ans += 1
                    continue
                for a, b in neighbors4(f, y, x):
                    if f[a][b] == f[y][x] + 1:
                        q.append((a, b))
print(ans)