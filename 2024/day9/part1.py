import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip()

idx = 0
s = []
for i in range(len(f)):
    if i % 2 == 0:
        for _ in range(int(f[i])):
            s.append(idx)
        idx += 1
    else :
        for _ in range(int(f[i])):
            s.append('.')

l, r = 0, len(s) - 1
while l < r:
    while s[l] != '.': l += 1
    while s[r] == '.': r -= 1
    if l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

ans = 0 
for i, x in enumerate(s):
    if x == '.': break
    ans += i * x
print(ans)