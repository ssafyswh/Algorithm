import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 2)
for i in range(1, N + 1):
    t, p = map(int, input().split())
    dp[i] = max(dp[i], dp[i - 1])
    if i + t <= N + 1:
        dp[i + t] = max(dp[i + t], dp[i] + p)

print(max(dp[-1], dp[-2]))