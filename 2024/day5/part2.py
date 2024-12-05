import os
from collections import defaultdict

with open(os.path.dirname(__file__) + "/input.in") as file:
    rules, f = list(map(lambda x: x.split('\n'), file.read().strip().split('\n\n')))
    rules = list(map(lambda x: list(map(int, x.split('|'))), rules))
    f = list(map(lambda x: list(map(int, x.split(','))), f))

depend = defaultdict(set)
for x, y in rules:
    depend[x].add(y)

def check(line):
    for i in range(len(line)):
        for j in range(i):
            if line[j] in depend[line[i]]:
                return False
    return True

def change(line):
    res = []
    for x in line:
        res.insert(0, x)
        idx = 0
        while idx + 1 < len(res) and res[idx + 1] not in depend[x]:
            res[idx], res[idx + 1] = res[idx + 1], res[idx]
            idx += 1
    return res

ans = 0
for line in f:
    if not check(line):
        ans += change(line)[len(line) // 2]
print(ans)