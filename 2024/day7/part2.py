import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')

def int_to_base3(n):
    ans = ""
    while n:
        ans += str(n % 3)
        n //= 3
    return ans[::-1]


def all_possible(values):
    res = []
    for i in range(3**(len(values) - 1)):
        n = int_to_base3(i)
        n = '0' * (len(values) - 1 - len(n)) + n
        eq = values[0]
        for i in range(len(n)):
            match n[i]:
                case '0': eq += values[i + 1]
                case '1': eq *= values[i + 1]
                case '2': eq = int(str(eq) + str(values[i + 1]))
        res.append(eq)
    return res

ans = 0
for line in f:
    left, right = line.split(': ')
    left = int(left)
    right = list(map(int, right.split()))
    if left in all_possible(right): ans += left
print(ans)