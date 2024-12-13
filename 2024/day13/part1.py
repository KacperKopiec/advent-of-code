import os
from math import inf

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n\n')

ans = 0
for machine in f:
    machine = machine.replace(',', '').split('\n')
    A = list(map(lambda x: int(x[2:]), machine[0].split()[2:]))
    B = list(map(lambda x: int(x[2:]), machine[1].split()[2:]))
    END = list(map(lambda x: int(x[2:]), machine[2].split()[1:]))

    mn_cost = inf
    for a in range(101):
        for b in range(101):
            x, y = a * A[0] + b * B[0], a * A[1] + b * B[1]
            if [x, y] == END: mn_cost = min(mn_cost, 3 * a + b)

    if mn_cost != inf: ans += mn_cost
print(ans)