from collections import deque


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[y][x] = 1
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = []
for y in range(M):
    for x in range(N):
        if board[y][x] == 0:
            area = 1
            board[y][x] = 1
            route = deque([(x, y)])
            while route:
                for _ in range(len(route)):
                    nx, ny = route.popleft()
                    for d in delta:
                        dx, dy = nx + d[1], ny + d[0]
                        if 0 <= dx < N and 0 <= dy < M:
                            if board[dy][dx] == 0:
                                board[dy][dx] = 1
                                route.append((dx, dy))
                                area += 1
            result.append(area)
print(len(result))
print(*sorted(result))