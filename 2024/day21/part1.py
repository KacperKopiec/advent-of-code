import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n')
    
k1 = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2)
}

k2 = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2)
}

def numeric(s):
    ans = ""
    y, x = 3, 2
    for c in s:
        i, j = k1[c]
        if y == 3 and j == 0:
            while y > i:
                y -= 1
                ans += '^'
            while x > j:
                x -= 1
                ans += '<'
        while x > j:
            x -= 1
            ans += '<'
        while y > i:
            y -= 1
            ans += '^'
        if x == 0 and i == 3:
            while x < j:
                x += 1
                ans += '>'
            while y < i:
                y += 1
                ans += 'v'
        while y < i:
            y += 1
            ans += 'v'
        while x < j:
            x += 1
            ans += '>'
        ans += 'A'
    return ans

def directional(s):
    ans = ""
    y, x = 0, 2
    for c in s:
        i, j = k2[c]
        while x > j:
            x -= 1
            ans += '<'
        while y < i:
            y += 1
            ans += 'v'
        while y > i:
            y -= 1
            ans += '^'
        while x < j:
            x += 1
            ans += '>'
        ans += 'A'
    return ans 

ans = 0
for code in f:
    n = int(code[:-1])
    code = directional(directional(numeric(code)))
    ans += len(code) * n
print(ans)