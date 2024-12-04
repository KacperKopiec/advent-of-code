import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')

ans = 0
for i in range(1, len(f) - 1):
    for j in range(1, len(f[i]) - 1):
        if f[i][j] == 'A':
            if set(['M', 'S']) == set([f[i - 1][j - 1], f[i + 1][j + 1]]) and set(['M', 'S']) == set([f[i - 1][j + 1], f[i + 1][j - 1]]): ans += 1
print(ans)