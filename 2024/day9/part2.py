import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip()

idx = 0
s = []
for i in range(len(f)):
    if i % 2 == 0:
        s.append([idx, int(f[i])])
        idx += 1
    else :
        s.append([-1, int(f[i])])

idx -= 1
while idx > 0:
    cur = 0
    for i in range(len(s)):
        if s[i][0] == idx:
            cur = i
            break
    
    for i in range(i):
        if s[i][0] == -1 and s[i][1] >= s[cur][1]:
            s[i][1] -= s[cur][1]
            cp = s[cur][:]
            s[cur][0] = -1
            s.insert(i, cp)
            break
    idx -= 1

res = []
for i in range(len(s)):
    if s[i][0] == -1:
        for _ in range(s[i][1]):
            res.append('.')
    else:
        for _ in range(s[i][1]):
            res.append(s[i][0])

ans = 0 
for i, x in enumerate(res):
    if x == '.': continue
    ans += i * x
print(ans)