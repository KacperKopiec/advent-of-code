import os
import re

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
def rotate(grid): return list(zip(*grid[::-1]))

pattern = r"XMAS"
ans = 0
for _ in range(4):
    for line in f:
        ans += len(re.findall(pattern, line))
    f = list(map(lambda x: ''.join(x), rotate(f)))

diagonals1 = []
for i in range(len(f) - 1, -1, -1):
    cur = ""
    y, x = i, 0
    while y < len(f) and x < len(f[0]):
        cur += f[y][x]
        x += 1
        y += 1
    while len(cur) != len(f[0]): cur += '.'
    diagonals1.append(cur)

for i in range(1, len(f[0])):
    cur = ""
    y, x = 0, i
    while y < len(f) and x < len(f[0]):
        cur += f[y][x]
        x += 1
        y += 1
    while len(cur) != len(f[0]): cur += '.'
    diagonals1.append(cur)

diagonals2 = []
for i in range(len(f) - 1, -1, -1):
    cur = ""
    y, x = i, len(f[0]) - 1
    while y < len(f) and x >= 0:
        cur += f[y][x]
        x -= 1
        y += 1
    while len(cur) != len(f[0]): cur += '.'
    diagonals2.append(cur)

for i in range(len(f[0]) - 2, -1, -1):
    cur = ""
    y, x = 0, i
    while y < len(f) and x >= 0:
        cur += f[y][x]
        x -= 1
        y += 1
    while len(cur) != len(f[0]): cur += '.'
    diagonals2.append(cur)

for _ in range(2):
    for line1, line2 in zip(diagonals1, diagonals2):
        ans += len(re.findall(pattern, line1))
        ans += len(re.findall(pattern, line2))
    diagonals1 = list(map(lambda x: ''.join(x), rotate(rotate(diagonals1))))
    diagonals2 = list(map(lambda x: ''.join(x), rotate(rotate(diagonals2))))
print(ans)