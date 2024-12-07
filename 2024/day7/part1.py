import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')

def all_possible(values):
    res = []
    for i in range(1 << (len(values) - 1)):
        n = bin(i)[2:]
        n = '0' * (len(values) - 1 - len(n)) + n
        eq = values[0]
        for i in range(len(n)):
            match n[i]:
                case '0': eq += values[i + 1]
                case '1': eq *= values[i + 1]
        res.append(eq)
    return res

ans = 0
for line in f:
    left, right = line.split(': ')
    left = int(left)
    right = list(map(int, right.split()))
    if left in all_possible(right): ans += left
print(ans)