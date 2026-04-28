import sys
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M = map(int, input().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
safe_count = 0
safe_area = []
virus = []
for y in range(N):
    for x in range(M):
        if lab[y][x] == 0:
            safe_count += 1
            safe_area.append((y, x))
        elif lab[y][x] == 2:
            virus.append((y, x))
combinations = []
for i in range(safe_count - 2):
    for j in range(i + 1, safe_count - 1):
        for k in range(j + 1, safe_count):
            combinations.append((safe_area[i], safe_area[j], safe_area[k]))
min_corrupted = safe_count
for case in combinations:
    flag = False
    for index in case:
        lab[index[0]][index[1]] = 1
    visited = [[0] * M for _ in range(N)]
    corrupted = 0
    for source in virus:
        infect = deque([source])
        visited[source[0]][source[1]] = 1
        while infect:
            ny, nx = infect.popleft()
            for d in delta:
                dy, dx = ny + d[0], nx + d[1]
                if 0 <= dy < N and 0 <= dx < M:
                    if not visited[dy][dx] and not lab[dy][dx]:
                        infect.append((dy, dx))
                        visited[dy][dx] = 1
                        corrupted += 1
            if corrupted > min_corrupted:
                flag = True
                break
        if flag:
            break
    min_corrupted = min(corrupted, min_corrupted)
    for index in case:
        lab[index[0]][index[1]] = 0
result = safe_count - min_corrupted - 3
print(result)