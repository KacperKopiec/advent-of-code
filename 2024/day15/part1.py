import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f, moves = file.read().strip().split('\n\n')
    f = list(map(list, f.split('\n')))
    
DIR_MAP = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '@':
            robot = [i, j]

for move in moves:
    if move == '\n': continue
    v = DIR_MAP[move]
    k = 1
    while f[robot[0] + k * v[0]][robot[1] + k * v[1]] == 'O': k += 1
    if f[robot[0] + k * v[0]][robot[1] + k * v[1]] != '#':
        for i in range(k, 0, -1):
            y1, x1 = robot[0] + i * v[0], robot[1] + i * v[1]
            y2, x2 = robot[0] + (i - 1) * v[0], robot[1] + (i - 1) * v[1]
            f[y1][x1], f[y2][x2] = f[y2][x2], f[y1][x1]
        robot = [robot[0] + v[0], robot[1] + v[1]]
    
ans = 0
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == 'O':
            ans += 100 * i + j
print(ans)
