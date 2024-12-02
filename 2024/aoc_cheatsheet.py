import re
import math
import itertools
from collections import *
import heapq
import functools
from copy import deepcopy

# DIRECTIONS
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIAGONALS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
ALL_DIRS = [(-1, 0), (-1, -1), (1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 1)]
DIR_MAP = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}

# GRID HELPERS
def in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def neighbors4(grid, row, col):
    for dr, dc in DIRECTIONS:
        rr, cc = row + dr, col + dc
        if in_bounds(grid, rr, cc):
            yield (rr, cc)

def neighbors8(grid, r, c):
    for dr, dc in ALL_DIRS:
        rr, cc = r + dr, c + dc
        if in_bounds(grid, rr, cc):
            yield (rr, cc)

# COMMON OPERATIONS
def transpose(grid): return list(zip(*grid))
def rotate(grid): return list(zip(*grid[::-1]))
def flatten(lst): return [item for sublist in lst for item in sublist]

# SEARCH/PATHS
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def bfs(grid, start, target=None):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        pos, dist = q.popleft()
        if pos == target:
            return dist
        for npos in neighbors4(grid, *pos):
            if npos not in seen:
                seen.add(npos)
                q.append((npos, dist + 1))
    return float('inf')

def dijkstra(grid, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, pos = heapq.heappop(pq)
        if d > dist[pos]:
            continue
        for npos, weight in neighbors4(grid, *pos):
            new_dist = dist[pos] + weight
            if new_dist < dist[npos]:
                dist[npos] = new_dist
                heapq.heappush(pq, (new_dist, npos))
    return dist


# MATH
MOD = 10**9 + 7
INF = math.inf
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def lcm_list(lst): return functools.reduce(lcm, lst)
def prod(lst): return functools.reduce(lambda x,y: x*y, lst)

# USEFUL SETS/RANGES
def range_intersection(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))

def range_union(r1, r2):
    if r1.stop < r2.start or r2.stop < r1.start:
        return None
    return range(min(r1.start, r2.start), max(r1.stop, r2.stop))