import sys
from collections import deque

delta_base = ((0, 1), (1, 0), (0, -1), (-1, 0))
delta_knight = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

K = int(input())
W, H = map(int, input().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

# y, x, K-remain, turn
MAX = float('inf')
visited = [[[MAX] * W for _ in range(H)] for _ in range(K + 1)]
visited[0][0][0] = 0
q = deque([(0, 0, 0, 0)])
while q:
    y, x, k, t = q.popleft()
    if y == H - 1 and x == W - 1:
        print(t)
        break
    for db in delta_base:
        dy, dx = y + db[0], x + db[1]
        if not (0 <= dy < H and 0 <= dx < W):
            continue
        if field[dy][dx]:
            continue
        if visited[k][dy][dx] <= t + 1:
            continue
        visited[k][dy][dx] = t + 1
        q.append((dy, dx, k, t + 1))
    if k >= K:
        continue
    for dk in delta_knight:
        dy, dx = y + dk[0], x + dk[1]
        if not (0 <= dy < H and 0 <= dx < W):
            continue
        if field[dy][dx]:
            continue
        if visited[k + 1][dy][dx] <= t + 1:
            continue
        visited[k + 1][dy][dx] = t + 1
        q.append((dy, dx, k + 1, t + 1))
else:
    print(-1)