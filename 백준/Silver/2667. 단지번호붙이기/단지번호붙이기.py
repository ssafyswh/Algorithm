from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
maps = [list(map(int, list(input()))) for _ in range(N)]
result1 = 0
result2 = []
for y in range(N):
    for x in range(N):
        if maps[y][x]:
            result1 += 1
            blocks = 1
            maps[y][x] = 0
            route = deque([(y, x)])
            while route:
                ny, nx = route.popleft()
                for d in delta:
                    dy, dx = ny + d[0], nx + d[1]
                    if 0 <= dy < N and 0 <= dx < N:
                        if maps[dy][dx]:
                            route.append((dy, dx))
                            maps[dy][dx] = 0
                            blocks += 1
            result2.append(blocks)
result2.sort()
print(result1)
for result in result2:
    print(result)