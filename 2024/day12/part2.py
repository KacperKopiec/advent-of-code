import os
from collections import deque
from math import inf
from copy import deepcopy

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
flag = [[0 for _ in range(len(f[0]))] for _ in range(len(f))]

def in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def neighbors4(grid, row, col):
    for dr, dc in DIRECTIONS:
        rr, cc = row + dr, col + dc
        if in_bounds(grid, rr, cc):
            yield (rr, cc)

ans, idx = 0, 1
for i in range(len(f)):
    for j in range(len(f[0])):
        if not flag[i][j]:
            area = 0
            q = deque()
            q.append((i, j))
            left_down, right_up = [inf, inf], [-inf, -inf]
            while len(q):
                y, x = q.popleft()
                if flag[y][x]: continue
                flag[y][x] = idx
                area += 1
                left_down[0] = min(left_down[0], y)
                left_down[1] = min(left_down[1], x)
                right_up[0] = max(right_up[0], y)
                right_up[1] = max(right_up[1], x)
                for a, b in neighbors4(f, y, x):
                    if f[y][x] == f[a][b] and not flag[a][b]: q.append((a, b))
            
            F = list(map(list, deepcopy(f)))
            for y in range(left_down[0], right_up[0] + 1):
                for x in range(left_down[1], right_up[1] + 1):
                    if flag[y][x] != idx:
                        F[y][x] = '.'
            idx += 1

            sides = 0
            # sweep line increasing y
            if F[left_down[0]][left_down[1]] == f[i][j]: sides += 1
            for x in range(left_down[1] + 1, right_up[1] + 1):
                if F[left_down[0]][x] != '.' and F[left_down[0]][x] != F[left_down[0]][x - 1]: sides += 1
            
            for y in range(left_down[0] + 1, right_up[0] + 1):
                changes1, changes2 = [], []
                for x in range(left_down[1], right_up[1] + 1):
                    if F[y][x] != F[y - 1][x]:
                        changes1.append(x) if F[y][x] == '.' else changes2.append(x)
                
                if changes1: sides += 1
                for k in range(1, len(changes1)):
                    if changes1[k - 1] + 1 != changes1[k]:
                        sides += 1

                if changes2: sides += 1
                for k in range(1, len(changes2)):
                    if changes2[k - 1] + 1 != changes2[k]:
                        sides += 1
            
            if F[right_up[0]][left_down[1]] == f[i][j]: sides += 1
            for x in range(left_down[1] + 1, right_up[1] + 1):
                if F[right_up[0]][x] != '.' and F[right_up[0]][x] != F[right_up[0]][x - 1]: sides += 1
            
            # sweep line increasing x
            if F[left_down[0]][left_down[1]] == f[i][j]: sides += 1
            for y in range(left_down[0] + 1, right_up[0] + 1):
                if F[y][left_down[1]] != '.' and F[y][left_down[1]] != F[y - 1][left_down[1]]: sides += 1
            
            for x in range(left_down[1] + 1, right_up[1] + 1):
                changes1, changes2 = [], []
                for y in range(left_down[0], right_up[0] + 1):
                    if F[y][x] != F[y][x - 1]:
                        changes1.append(y) if F[y][x] == '.' else changes2.append(y)
                
                if changes1: sides += 1
                for k in range(1, len(changes1)):
                    if changes1[k - 1] + 1 != changes1[k]:
                        sides += 1

                if changes2: sides += 1
                for k in range(1, len(changes2)):
                    if changes2[k - 1] + 1 != changes2[k]:
                        sides += 1
            
            if F[left_down[0]][right_up[1]] == f[i][j]: sides += 1
            for y in range(left_down[0] + 1, right_up[0] + 1):
                if F[y][right_up[1]] != '.' and F[y][right_up[1]] != F[y - 1][right_up[1]]: sides += 1
            
            ans += area * sides
print(ans)