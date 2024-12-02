import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = list(map(lambda x: x.split(), file.read().strip().split('\n')))

l, r = [], []
for x, y in f:
    l.append(int(x))
    r.append(int(y))

l.sort()
r.sort()

print(sum(abs(x - y) for x, y in zip(l, r)))