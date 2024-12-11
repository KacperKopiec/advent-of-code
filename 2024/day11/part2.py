import os
from collections import defaultdict

with open(os.path.dirname(__file__) + "/input.in") as file:
    d = defaultdict(int)
    f = list(map(int, file.read().strip().split()))
    for x in f:
        d[x] += 1

for _ in range(75):
    nxt = defaultdict(int)
    for x, y in d.items():
        if x == 0:
            nxt[1] += y
        elif len(str(x)) % 2 == 0:
            nxt[int(str(x)[:len(str(x))//2])] += y
            nxt[int(str(x)[len(str(x))//2:])] += y
        else:
            nxt[x * 2024] += y
    d = nxt
print(sum(d.values()))