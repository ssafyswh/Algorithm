import sys
sys.setrecursionlimit(10**6)

M, N = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
dp = [[-1] * N for _ in range(M)]

def dfs(y, x):
    if y == 0 and x == 0:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    height = maps[y][x]
    for d in delta:
        dy, dx = y + d[0], x + d[1]
        if not (0 <= dy < M and 0 <= dx < N):
            continue
        if height < maps[dy][dx]:
            dp[y][x] += dfs(dy, dx)
    return dp[y][x]

print(dfs(M - 1, N - 1))