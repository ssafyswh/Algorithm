import sys
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for y in range(n):
    for x in range(m):
        if maps[y][x] == 1:
            maps[y][x] = -1
        elif maps[y][x] == 2:
            maps[y][x] = 0
            start_y, start_x = y, x
route = deque([(start_y, start_x)])
count = 0
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while route:
    count += 1
    for _ in range(len(route)):
        ny, nx = route.popleft()
        for d in delta:
            dy, dx = ny + d[0], nx + d[1]
            if 0 <= dy < n and 0 <= dx < m:
                if maps[dy][dx] == -1:
                    maps[dy][dx] = count
                    route.append((dy, dx))
for row in maps:
    print(*row)