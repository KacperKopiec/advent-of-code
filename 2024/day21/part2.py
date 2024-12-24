import os
from itertools import pairwise

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

def path(start, end):
    ans = ""
    y, x = k2[start]
    i, j = k2[end]
    if y == 0 and i == 1 and j == 0:
        while y < i:
            y += 1
            ans += 'v'
    while x > j:
        x -= 1
        ans += '<'
    while y < i:
        y += 1
        ans += 'v'
    if y == 1 and x == 0 and i == 0:
        while x < j:
            x += 1
            ans += '>'
    while y > i:
        y -= 1
        ans += '^'
    while x < j:
        x += 1
        ans += '>'
    ans += 'A'
    return ans 

cache = dict()
def solve(start, end, depth = 1, max_depth = 25):
    if (start, end, depth) in cache.keys():
        return cache[(start, end, depth)]
    if depth == max_depth:
        cache[(start, end, depth)] = len(path(start, end))
        return cache[(start, end, depth)]
    
    cache[(start, end, depth)] = solve('A', path(start, end)[0], depth + 1)
    for s in pairwise(path(start, end)):
        cache[(start, end, depth)] += solve(s[0], s[1], depth + 1)
    return cache[(start, end, depth)]

ans = 0
for code in f:
    n = int(code[:-1])
    code = numeric(code)

    sum = solve('A', code[0])
    for s in pairwise(code):
        sum += solve(s[0], s[1])
    ans += sum * n
print(ans)