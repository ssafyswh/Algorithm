import sys
from collections import deque


N = int(input())
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
picture = [sys.stdin.readline() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result1 = 0
for y in range(N):
    for x in range(N):
        if visited[y][x]:
            continue
        result1 += 1
        route = deque([(y, x)])
        visited[y][x] = 1
        while route:
            for _ in range(len(route)):
                ny, nx = route.popleft()
                for d in delta:
                    dy, dx = ny + d[0], nx + d[1]
                    if 0 <= dy < N and 0 <= dx < N:
                        if not visited[dy][dx] and picture[ny][nx] == picture[dy][dx]:
                            visited[dy][dx] = 1
                            route.append((dy, dx))
visited = [[0] * N for _ in range(N)]
result2 = 0
for y in range(N):
    for x in range(N):
        if visited[y][x]:
            continue
        result2 += 1
        route = deque([(y, x)])
        visited[y][x] = 1
        if picture[y][x] != 'B':
            color = 'RG'
        else:
            color = 'B'
        while route:
            for _ in range(len(route)):
                ny, nx = route.popleft()
                for d in delta:
                    dy, dx = ny + d[0], nx + d[1]
                    if 0 <= dy < N and 0 <= dx < N:
                        if not visited[dy][dx] and picture[dy][dx] in color:
                            visited[dy][dx] = 1
                            route.append((dy, dx))
print(result1, result2)