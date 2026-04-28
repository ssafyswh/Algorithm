import sys
from collections import deque


T = int(input())
delta = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
for _ in range(T):
    I = int(input())
    board = [[0] * I for _ in range(I)]
    sy, sx = map(int, sys.stdin.readline().split())
    gy, gx = map(int, sys.stdin.readline().split())
    route = deque([(sy, sx)])
    board[sy][sx] = 1
    result = 0
    ny, nx = sy, sx
    flag = False
    while ny != gy or nx != gx:
        result += 1
        for _ in range(len(route)):
            ny, nx = route.popleft()
            for d in delta:
                dy, dx = ny + d[0], nx + d[1]
                if dy == gy and dx == gx:
                    flag = True
                    break
                if 0 <= dy < I and 0 <= dx < I:
                    if not board[dy][dx]:
                        route.append((dy, dx))
                        board[dy][dx] = 1
            if flag:
                break
        if flag:
            break
    print(result)