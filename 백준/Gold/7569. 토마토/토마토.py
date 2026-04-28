import sys
from collections import deque

delta = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]  # (z, y, x)
M, N, H = map(int, input().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
tomato = []
remain = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                remain += 1
            elif box[z][y][x] == 1:
                tomato.append((z, y, x))

result = 0
ripen = deque(tomato)
while ripen:
    check = False
    for _ in range(len(ripen)):
        nz, ny, nx = ripen.popleft()
        for d in delta:
            dz, dy, dx = nz + d[0], ny + d[1], nx + d[2]
            if 0 <= dz < H and 0 <= dy < N and 0 <= dx < M:
                if box[dz][dy][dx] == 0:
                    check = True
                    remain -= 1
                    ripen.append((dz, dy, dx))
                    box[dz][dy][dx] = 1
    if check:
        result += 1
if remain:
    result = -1
print(result)