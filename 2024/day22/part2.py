import os
from itertools import product

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = list(map(int, file.read().strip().split('\n')))
    
ans = dict()
for a, b, c, d in product(range(-10, 11), range(-10, 11), range(-10, 11), range(-10, 11)):
    ans[(a, b, c, d)] = 0

for n in f:
    bananas = [n % 10]
    s = set()
    for _ in range(2000):
        n = (n ^ (n * 64)) % 16777216
        n = (n ^ (n // 32)) % 16777216
        n = (n ^ (n * 2048)) % 16777216
        bananas.append(n % 10)
    
    q = []
    for i in range(1, len(bananas)):
        q.append(bananas[i] - bananas[i - 1])
        if len(q) == 5: q.pop(0)
        if len(q) == 4 and tuple(q) not in s:
            ans[tuple(q)] += bananas[i]
            s.add(tuple(q))
print(max(ans.values()))