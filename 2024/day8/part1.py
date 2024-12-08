import os
from collections import defaultdict
import itertools

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
antenas = defaultdict(list)
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] != '.':
            antenas[f[i][j]].append((i, j))

def in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

ans = set()
for values in antenas.values():
    for a, b in itertools.combinations(values, 2):
        v = (b[0] - a[0], b[1] - a[1])
        skalar = 0
        while in_bounds(f, b[0] + skalar * v[0], b[1] + skalar * v[1]): 
            ans.add((b[0] + skalar * v[0], b[1] + skalar * v[1]))
            skalar += 1
        skalar = 0
        while in_bounds(f, a[0] - skalar * v[0], a[1] - skalar * v[1]): 
            ans.add((a[0] - skalar * v[0], a[1] - skalar * v[1]))
            skalar += 1

print(len(ans))
