import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    A = int(f[0].split()[2])
    B = int(f[1].split()[2])
    C = int(f[2].split()[2])
    f = list(map(int, f[4].split()[1].split(',')))

ans = [-1] * (len(f) * 3)
ans += [0] * len(f)
res = float('inf')
def solve(idx = 0):
    if idx == 48:
        global res
        res = min(res, int(''.join(list(map(str, ans[::-1]))), 2))
        return 
    
    b = f[idx // 3]
    for mask in range(1 << 3):
        B = mask ^ 5
        C = mask ^ b

        if ans[B + idx] != -1 and ans[B + idx] != int(C & 1 == 1): continue
        if ans[B + idx + 1] != -1 and ans[B + idx + 1] != int(C & 2 == 2): continue
        if ans[B + idx + 2] != -1 and ans[B + idx + 2] != int(C & 4 == 4): continue
        xd = B + idx
        tmp2 = [ans[B + idx], ans[B + idx + 1], ans[B + idx + 2]]
        ans[xd] = int(C & 1 == 1)
        ans[xd + 1] = int(C & 2 == 2)
        ans[xd + 2] = int(C & 4 == 4)

        B ^= 3
        good = True
        if ans[idx] != -1 and ans[idx] != int(B & 1 == 1): good = False
        if ans[idx + 1] != -1 and ans[idx + 1] != int(B & 2 == 2): good = False
        if ans[idx + 2] != -1 and ans[idx + 2] != int(B & 4 == 4): good = False

        if not good:
            ans[xd] = tmp2[0]
            ans[xd + 1] = tmp2[1]
            ans[xd + 2] = tmp2[2]
            continue

        tmp1 = [ans[idx], ans[idx + 1], ans[idx + 2]]

        ans[idx] = int(B & 1 == 1)
        ans[idx + 1] = int(B & 2 == 2)
        ans[idx + 2] = int(B & 4 == 4)
        
        solve(idx + 3)

        ans[idx] = tmp1[0]
        ans[idx + 1] = tmp1[1]
        ans[idx + 2] = tmp1[2]
        ans[xd] = tmp2[0]
        ans[xd + 1] = tmp2[1]
        ans[xd + 2] = tmp2[2]

solve()
print(res)