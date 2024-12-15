import os
from collections import deque

with open(os.path.dirname(__file__) + "/input.in") as file:
    F, moves = file.read().strip().split('\n\n')
    F = list(map(list, F.split('\n')))
    
DIR_MAP = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

f = [[] for _ in range(len(F))]
for i in range(len(F)):
    for j in range(len(F[0])):
        match F[i][j]:
            case '#': f[i] += ['#', '#']
            case 'O': f[i] += ['[', ']']
            case '.': f[i] += ['.', '.']
            case '@': f[i] += ['@', '.']

for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '@':
            robot = [i, j]

for move in moves:
    if move == '\n': continue
    v = DIR_MAP[move]
    box = [(robot[0], robot[1])]
    if f[robot[0] + v[0]][robot[1] + v[1]] in '[]':
        flag = [[False for _ in range(len(f[0]))] for _ in range(len(f))]
        q = deque()
        q.append((robot[0] + v[0], robot[1] + v[1]))
        while len(q):
            y, x = q.popleft()
            if flag[y][x]: continue
            flag[y][x] = True
            box.append((y, x))
            
            if f[y][x] == '[' and not flag[y][x + 1]: q.append((y, x + 1))
            if f[y][x] == ']' and not flag[y][x - 1]: q.append((y, x - 1))

            if f[y + v[0]][x + v[1]] in '[]' and not flag[y + v[0]][x + v[1]]:
                q.append((y + v[0], x + v[1]))

        good = True
        for b in box:
            if f[b[0] + v[0]][b[1] + v[1]] == '#':
                good = False
        
        if good:
            for b in box[::-1]:
                y, x = b[0] + v[0], b[1] + v[1]
                a, b = b[0], b[1]
                f[a][b], f[y][x] = f[y][x], f[a][b]
            robot = [robot[0] + v[0], robot[1] + v[1]]
    elif f[robot[0] + v[0]][robot[1] + v[1]] == '.':
        y, x = robot[0] + v[0], robot[1] + v[1]
        a, b = robot[0], robot[1]
        f[a][b], f[y][x] = f[y][x], f[a][b]
        robot = [robot[0] + v[0], robot[1] + v[1]]

ans = 0
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '[':
            ans += 100 * i + j
print(ans)
