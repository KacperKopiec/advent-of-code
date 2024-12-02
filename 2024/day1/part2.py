import os
from collections import Counter

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = list(map(lambda x: x.split(), file.read().strip().split('\n')))

l, r = [], []
for x, y in f:
    l.append(int(x))
    r.append(int(y))

cnt = Counter(r)

print(sum(x * cnt[x] for x in l))