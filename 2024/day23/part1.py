import os
from itertools import combinations

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
computers = set()
g = dict()
for line in f:
    a, b = line.split('-')
    computers.add(a)
    computers.add(b)
    if a not in g.keys(): g[a] = set()
    if b not in g.keys(): g[b] = set()
    g[a].add(b)
    g[b].add(a)

ans = 0
for a, b, c in combinations(computers, 3):
    if b in g[a] and c in g[a] and c in g[b]:
        if a[0] == 't' or b[0] == 't' or c[0] == 't':
            ans += 1
print(ans)