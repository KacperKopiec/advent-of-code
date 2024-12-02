import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')

def check(line):
    r = []
    for i in range(1, len(line)):
        r.append(line[i] - line[i - 1])
    
    for i in range(1, len(r)):
        if r[i] * r[i - 1] < 0:
            return False
    
    for x in r:
        if x == 0 or 3 < abs(x):
            return False
    
    return True

ans = 0
for line in f:
    line = list(map(int, line.split()))
    if check(line): ans += 1
    
print(ans)