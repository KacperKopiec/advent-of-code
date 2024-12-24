import os
from collections import deque, defaultdict

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n\n')
    gates, gate, g, q, type, signals = set(), dict(), defaultdict(list), deque(), dict(), defaultdict(list)
    for line in f[0].split('\n'):
        a, b = line.split(': ')
        gate[a] = int(b)
        gates.add(a)
        type[a] = -1
        q.append(a)

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

ans = ""
for g in sorted(res, reverse=True):
    ans += str(gate[g])

print(int(ans, 2))