import sys
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
M, N = map(int, input().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tomato = []
remain = 0
for y in range(N):
    for x in range(M):
        if box[y][x] == 0:
            remain += 1
        elif box[y][x] == 1:
            tomato.append((y, x))

result = 0
ripen = deque(tomato)
while ripen:
    check = False
    for _ in range(len(ripen)):
        ny, nx = ripen.popleft()
        for d in delta:
            dy, dx = ny + d[0], nx + d[1]
            if 0 <= dy < N and 0 <= dx < M:
                if box[dy][dx] == 0:
                    check = True
                    remain -= 1
                    ripen.append((dy, dx))
                    box[dy][dx] = 1
    if check:
        result += 1
if remain:
    result = -1
print(result)