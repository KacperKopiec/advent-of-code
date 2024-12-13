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
    END[0] += 10000000000000
    END[1] += 10000000000000

    det = A[0] * B[1] - A[1] * B[0]
    if det == 0: continue

    a, b = (END[0] * B[1] - B[0] * END[1]) // det, (A[0] * END[1] - END[0] * A[1]) // det
    x, y = a * A[0] + b * B[0], a * A[1] + b * B[1]
    if [x, y] == END: ans += 3 * a + b
print(ans)