import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().strip() for _ in range(N)]

E = [[0] * (M + 1) for _ in range(N + 1)]
for y in range(N):
    for x in range(M):
        E[y + 1][x + 1] = (1 if matrix[y][x] == 'E' else 0) + E[y + 1][x] + E[y][x + 1] - E[y][x]

ES = [[0] * (M + 1) for _ in range(N + 1)]
for y in range(N):
    for x in range(M):
        ES[y + 1][x + 1] = (E[y + 1][x + 1] if matrix[y][x] == 'S' else 0) + ES[y + 1][x] + ES[y][x + 1] - ES[y][x]

result = 0
for y in range(N):
    for x in range(M):
        if matrix[y][x] != 'M':
            continue
        result += ES[y + 1][x + 1]

modular = 10 ** 9 + 7
print(result % modular)