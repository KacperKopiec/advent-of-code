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

ans = 0
for line in f:
    if check(line):
        ans += line[len(line) // 2]
print(ans)