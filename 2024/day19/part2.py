import os

with open(os.path.dirname(__file__) + "/input.in") as file:
    f = file.read().strip().split('\n\n')
    towels = f[0].split(', ')
    patterns = f[1].split('\n')
    
d = {'w': 0, 'u' : 1, 'b': 2, 'r': 3, 'g': 4}

class Node:
    def __init__(self):
        self.next = [None] * 5
        self.flag = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        cur = self.root
        for c in s:
            if cur.next[d[c]] == None:
                cur.next[d[c]] = Node()
            cur = cur.next[d[c]]
        cur.flag = True

T = Trie()

def check(s):
    s = '#' + s
    dp = [0] * len(s)
    dp[0] = 1
    for i in range(1, len(s)):
        cur, j = T.root, i
        while j >= 1 and cur.next[d[s[j]]] != None:
            cur = cur.next[d[s[j]]]
            if cur.flag: dp[i] += dp[j - 1]
            j -= 1
    return dp[-1]

for towel in towels:
    T.insert(towel[::-1])

print(sum(check(pattern) for pattern in patterns))