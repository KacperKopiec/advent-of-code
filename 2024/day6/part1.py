import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
DIR_MAP = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}
def in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] != '.' and f[i][j] != '#':
            start = (i, j)
            break

dir = f[start[0]][start[1]]

ans = set()
while in_bounds(f, start[0], start[1]):
    ans.add(start)
    v = DIR_MAP[dir]
    nxt = (start[0] + v[0], start[1] + v[1])
    if in_bounds(f, nxt[0], nxt[1]) and f[nxt[0]][nxt[1]] == '#':
        match dir:
            case '^': dir = '>'
            case '>': dir = 'v'
            case 'v': dir = '<'
            case '<': dir = '^'
        continue
    start = nxt

print(len(ans))