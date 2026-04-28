import sys
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
h, w = map(int, input().split())
maps = [list(sys.stdin.readline()) for _ in range(h)]
visited = [[0] * w for _ in range(h)]
islands = {}
number = 0
for y in range(h):
    for x in range(w):
        if not visited[y][x] and maps[y][x] == 'L':
            visited[y][x] = 1
            route = deque([(y, x)])
            number += 1
            islands[number] = [(y, x)]
            while route:
                for _ in range(len(route)):
                    ny, nx = route.popleft()
                    for d in delta:
                        dy, dx = ny + d[0], nx + d[1]
                        if 0 <= dy < h and 0 <= dx < w:
                            if not visited[dy][dx] and maps[dy][dx] == 'L':
                                route.append((dy, dx))
                                visited[dy][dx] = 1
                                islands[number].append((dy, dx))
treasure = [0] * number
for i in range(number):
    island = islands[i + 1]
    area = len(island)
    max_distance = 0
    for j in range(area):
        visited = [[0] * w for _ in range(h)]
        sy, sx = island[j]
        visited[sy][sx] = 1
        search = deque([(sy, sx)])
        distance = 0
        while search:
            count = 0
            for _ in range(len(search)):
                nny, nnx = search.popleft()
                for d in delta:
                    ddy, ddx = nny + d[0], nnx + d[1]
                    if 0 <= ddy < h and 0 <= ddx < w:
                        if not visited[ddy][ddx] and maps[ddy][ddx] == 'L':
                            search.append((ddy, ddx))
                            visited[ddy][ddx] = 1
                            count += 1
            if count:
                distance += 1
        max_distance = max(max_distance, distance)
    treasure[i] = max_distance
print(max(treasure))