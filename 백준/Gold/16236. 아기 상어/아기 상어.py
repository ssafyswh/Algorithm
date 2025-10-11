import sys
from collections import deque


def find_start():
    for y in range(N):
        for x in range(N):
            if sea[y][x] == 9:
                sea[y][x] = 0
                return y, x

def catch_fish():
    global sy, sx, size, count
    visited = [[False] * N for _ in range(N)]
    visited[sy][sx] = True
    q = deque([(0, sy, sx)])
    fish = []
    min_time = float('inf')

    while q:
        time, ny, nx = q.popleft()
        nxt_time = time + 1
        if time > min_time:
            break
        for d1, d2 in delta:
            dy, dx = ny + d1, nx + d2
            if not (0 <= dy < N and 0 <= dx < N):
                continue
            if visited[dy][dx]:
                continue
            if sea[dy][dx] > size:
                continue
            visited[dy][dx] = True

            if 0 < sea[dy][dx] < size:
                if nxt_time < min_time:
                    fish = [(dy, dx)]
                    min_time = nxt_time
                elif nxt_time == min_time:
                    fish.append((dy, dx))
            else:
                q.append((nxt_time, dy, dx))
    if fish:
        fish.sort(key=lambda x: (x[0], x[1]))
        fy, fx = fish[0]
        sea[fy][fx] = 0
        sy, sx = fy, fx
        count -= 1
        if count == 0:
            size += 1
            count = size
        return min_time
    else:
        return 0


def solve():
    result = 0
    while True:
        time = catch_fish()
        if time == 0:
            break
        result += time
    return result

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
size, count = 2, 2
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sy, sx = find_start()
print(solve())