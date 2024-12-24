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

best = []
def solve(clique, possible):
    global best
    if len(clique) + len(possible) <= len(best): return
    if len(best) < len(clique): best = clique[:]
    for v in possible:
        clique.append(v)
        solve(clique, possible & g[v])
        clique.pop()
solve([], computers)

print(','.join(sorted(best)))