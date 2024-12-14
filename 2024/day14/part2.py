import os
from copy import deepcopy

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
W, H = 101, 103
s = 7083 # Hardcoded solution, manually discovered
T = [[' ' for _ in range(W)] for _ in range(H)]

for line in f:
    p, v = list(map(lambda x: list(map(int, x[2:].split(','))), line.split(' ')))
    x, y = ((p[0] + s * v[0]) % W, (p[1] + s * v[1]) % H)
    T[y][x] = '#'

for line in T:
    print(''.join(line))