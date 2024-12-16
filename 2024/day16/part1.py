import os
from math import inf
from queue import PriorityQueue

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == 'S':
            start = (i, j)
        if f[i][j] == 'E':
            end = (i, j)

dist = [[[inf for _ in range(4)] for _ in range(len(f[0]))] for _ in range(len(f))]
q = PriorityQueue()
q.put((0, start[0], start[1], 3))
while not q.empty():
    d, y, x, o = q.get()
    if dist[y][x][o] != inf: continue
    dist[y][x][o] = d

    if dist[y][x][(o - 1) % 4] == inf: q.put((d + 1000, y, x, (o - 1) % 4))
    if dist[y][x][(o + 1) % 4] == inf: q.put((d + 1000, y, x, (o + 1) % 4))

    match o:
        case 0: v = (-1, 0)
        case 1: v = (0, -1)
        case 2: v = (1, 0)
        case 3: v = (0, 1)
    
    y += v[0]
    x += v[1]
    if 0 <= y < len(f) and 0 <= x < len(f[0]) and f[y][x] != '#' and dist[y][x][o] == inf:
        q.put((d + 1, y, x, o))
        
print(min(dist[end[0]][end[1]]))