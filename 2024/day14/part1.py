import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
W, H = 101, 103
SEC = 100

ans = [0, 0, 0, 0]
for line in f:
    p, v = list(map(lambda x: list(map(int, x[2:].split(','))), line.split(' ')))
    x, y = ((p[0] + SEC * v[0]) % W, (p[1] + SEC * v[1]) % H)
    if x < W // 2 and y < H // 2: ans[0] += 1
    if x < W // 2 and y > H // 2: ans[1] += 1
    if x > W // 2 and y < H // 2: ans[2] += 1
    if x > W // 2 and y > H // 2: ans[3] += 1
print(ans[0] * ans[1] * ans[2] * ans[3])