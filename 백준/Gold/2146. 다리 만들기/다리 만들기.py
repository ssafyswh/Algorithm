import sys
from collections import deque

def find_land():
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 1:
                return y, x
    return -1, -1

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

N = int(input())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def find_shore(y, x):
    _shore = set()
    maps[y][x] = 2
    q = deque([(y, x)])
    while q:
        ny, nx = q.popleft()
        for d in delta:
            dy, dx = ny + d[0], nx + d[1]
            if not (0 <= dy < N and 0 <= dx < N):
                continue
            if maps[dy][dx] == 0:
                _shore.add((ny, nx, 0))
            elif maps[dy][dx] == 1:
                q.append((dy, dx))
                maps[dy][dx] = 2
    return list(_shore)

def build_bridge(start):
    q = deque(start)
    visited = [[False] * N for _ in range(N)]
    while q:
        ny, nx, dist = q.popleft()
        for d in delta:
            dy, dx = ny + d[0], nx + d[1]
            if not (0 <= dy < N and 0 <= dx < N):
                continue
            if visited[dy][dx]:
                continue
            if maps[dy][dx] == 1:
                return dist, dy, dx
            if maps[dy][dx] == 0:
                visited[dy][dx] = True
                q.append((dy, dx, dist + 1))
    return -1, -1, -1

result = 10000
sy, sx = find_land()
while True:
    shore = find_shore(sy, sx)
    bridge, sy, sx = build_bridge(shore)
    if sy == -1:
        break
    result = min(result, bridge)
print(result)