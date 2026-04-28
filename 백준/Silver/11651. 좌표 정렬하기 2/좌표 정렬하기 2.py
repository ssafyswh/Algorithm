N = int(input())
grids = []
for _ in range(N):
    x, y = map(int, input().split())
    grids.append((x, y))
grids.sort(key=lambda x: (x[1], x[0]))
for grid in grids:
    print(*grid)