import sys

while True:
    N = int(input())
    if N == 0:
        break
    W, H = map(int, input().split())
    grid = [[0] * (W + 1) for _ in range(H + 1)]
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        grid[y][x] = 1
    result = 0
    S, T = map(int, input().split())
    for sy in range(1, H - T + 2):
        for sx in range(1, W - S + 2):
            persimmon = 0
            for dy in range(T):
                for dx in range(S):
                    if grid[sy + dy][sx + dx]:
                        persimmon += 1
            result = max(result, persimmon)
    print(result)