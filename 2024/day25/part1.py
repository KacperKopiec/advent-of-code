import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = list(map(lambda x: x.split('\n'), file.read().strip().split('\n\n')))
    
locks, keys = [], []
for line in f:
    if line[0][0] == '#':
        heigh = [0] * len(line[0])
        for j in range(len(line[0])):
            for i in range(len(line)):
                if line[i][j] == '#':
                    heigh[j] += 1
                else: break
        locks.append(heigh)
    else:
        heigh = [0] * len(line[0])
        for j in range(len(line[0])):
            for i in range(len(line) - 1, -1, -1):
                if line[i][j] == '#':
                    heigh[j] += 1
                else: break
        keys.append(heigh)

ans = 0
for key in keys:
    for lock in locks:
        good = True
        for x, y in zip(key, lock):
            if x + y > len(f[0]):
                good = False
                break
        if good: ans += 1
print(ans)