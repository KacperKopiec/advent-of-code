import os
from collections import deque, defaultdict
from itertools import combinations

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n\n')
    gates, gate, g, q, type, signals, edges = set(), defaultdict(int), defaultdict(list), deque(), dict(), defaultdict(list), []
    reverse_g = defaultdict(list)
    for line in f[0].split('\n'):
        a, b = line.split(': ')
        gate[a] = int(b)
        gates.add(a)
        type[a] = -1

    for line in f[1].split('\n'):
        line = line.split()
        gates.add(line[0])
        gates.add(line[2])
        gates.add(line[4])
        
        match line[1]:
            case 'AND': type[line[4]] = 0
            case 'OR': type[line[4]] = 1
            case 'XOR': type[line[4]] = 2

        g[line[0]].append(line[4])
        g[line[2]].append(line[4])
        reverse_g[line[4]].append(line[0])
        reverse_g[line[4]].append(line[2])

        edges.append([line[0], line[2], line[4], type[line[4]]])
    
def debug_backwards(g, depth = 3):
    for a, b, c, t in edges:
        type[c] = t

    qu = deque()
    qu.append((0, g))
    while len(qu):
        d, v = qu.popleft()
        if d == depth: continue

        for e in reverse_g[v]:
            print(f"{e}:[{gate[e]}] -- {type[v]} --> {v}:[{gate[v]}]")
            qu.append((d + 1, e))

def debug_forwards(gq, depth = 3):
    for a, b, c, t in edges:
        type[c] = t

    qu = deque()
    qu.append((0, gq))
    while len(qu):
        d, v = qu.popleft()
        if d == depth: continue

        for e in g[v]:
            print(f"{v}:[{gate[v]}] -- {type[e]} --> {e}:[{gate[e]}]")
            qu.append((d + 1, e))

def simulate():
    for i in range(45):
        s = str(i)
        if i < 10: s = '0' + s
        gate['x' + s] = 1
        gate['y' + s] = 0
        type['x' + s] = -1
        type['y' + s] = -1

        q.append('x' + s)
        q.append('y' + s)
    
    g = defaultdict(list)
    for a, b, c, t in edges:
        g[a].append(c)
        g[b].append(c)
        type[c] = t

    while len(q):
        cur = q.popleft()

        match type[cur]:
            case -1:
                for e in g[cur]:
                    signals[e].append(gate[cur])
                    if len(signals[e]) == 2: q.append(e)
            case 0:
                gate[cur] = signals[cur][0] & signals[cur][1]
                type[cur] = -1
                q.append(cur)
            case 1:
                gate[cur] = signals[cur][0] | signals[cur][1]
                type[cur] = -1
                q.append(cur)
            case 2:
                gate[cur] = signals[cur][0] ^ signals[cur][1]
                type[cur] = -1
                q.append(cur)

    res = []
    for g in gates:
        if g.startswith('z'):
            res.append(g)

    for g in sorted(res):
        print(g, gate[g])

simulate()

# used debug_backwards and debug_forwards to manually find switched edges in adder
# since i was adding x = 2^n - 1, y = 0 it was easy to see where it was making mistakes
swaped = ['z17', 'cmv', 'z23', 'rmj', 'z30', 'rdg', 'btb', 'mwp']
print(','.join(sorted(swaped)))