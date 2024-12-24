import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = list(map(int, file.read().strip().split('\n')))
    
ans = 0
for n in f:
    for _ in range(2000):
        n = (n ^ (n * 64)) % 16777216
        n = (n ^ (n // 32)) % 16777216
        n = (n ^ (n * 2048)) % 16777216
    ans += n
print(ans)
