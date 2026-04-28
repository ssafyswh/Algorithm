pipe = [(0, 1), (1, 1), (1, 0)]

def push(r, c, direct):
    if dp[r][c][direct] != -1:
        return dp[r][c][direct]
    if r == N - 1 and c == N - 1:
        return 1
    ways = 0
    if diag_check(r, c):
        ways += push(r + 1, c + 1, 1)
    if direct == 0 or direct == 1:
        if c + 1 < N and not room[r][c + 1]:
            ways += push(r, c + 1, 0)
    if direct == 1 or direct == 2:
        if r + 1 < N and not room[r + 1][c]:
            ways += push(r + 1, c, 2)
    dp[r][c][direct] = ways
    return ways

def diag_check(y, x):
    for d in pipe:
        dy, dx = y + d[0], x + d[1]
        if 0 <= dy < N and 0 <= dx < N and not room[dy][dx]:
            pass
        else:
            return False
    return True

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
dp = [[[-1] * 3 for _ in range(N)] for _ in range(N)]
print(push(0, 1, 0))