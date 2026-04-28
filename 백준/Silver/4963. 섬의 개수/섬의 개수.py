import sys
from collections import deque


delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
while True:
    w, h = map(int, sys.stdin.readline().split())
    if [w, h] == [0, 0]:
        break
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    result = 0
    for y in range(h):
        for x in range(w):
            if maps[y][x]:
                result += 1
                maps[y][x] = 0
                search = deque([(y, x)])
                while search:
                    ny, nx = search.popleft()
                    for d in delta:
                        dy, dx = ny + d[0], nx + d[1]
                        if 0 <= dy < h and 0 <= dx < w:
                            if maps[dy][dx]:
                                search.append((dy, dx))
                                maps[dy][dx] = 0
    print(result)