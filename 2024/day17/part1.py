import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    A = int(f[0].split()[2])
    B = int(f[1].split()[2])
    C = int(f[2].split()[2])
    f = list(map(int, f[4].split()[1].split(',')))

A = 236548287712877
idx = 0
out = []
while idx < len(f):
    x, y = f[idx], f[idx + 1]
    match x: # 2,4  1,3  7,5  1,5  0,3  4,3  5,5  3,0
        case 0:
            match y:
                case 0 | 1 | 2 | 3: A = A // 2**y
                case 4: A = A // 2**A
                case 5: A = A // 2**B
                case 6: A = A // 2**C
        case 1:
            B ^= y
        case 2:
            match y:
                case 0 | 1 | 2 | 3: B = y % 8
                case 4: B = A % 8
                case 5: B = B % 8
                case 6: B = C % 8
        case 3:
            if A:
                idx = y
                continue
        case 4:
            B ^= C
        case 5:
            match y:
                case 0 | 1 | 2 | 3: out.append(y % 8)
                case 4: out.append(A % 8)
                case 5: out.append(B % 8)
                case 6: out.append(C % 8)
        case 6:
            match y:
                case 0 | 1 | 2 | 3: B = A // 2**y
                case 4: B = A // 2**A
                case 5: B = A // 2**B
                case 6: B = A // 2**C
        case 7:
            match y:
                case 0 | 1 | 2 | 3: C = A // 2**y
                case 4: C = A // 2**A
                case 5: C = A // 2**B
                case 6: C = A // 2**C
    idx += 2
print(','.join(list(map(str, out))))