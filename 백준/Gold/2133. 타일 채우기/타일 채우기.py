N = int(input())
dp = [[0, 0] for _ in range(N + 1)]
if N >= 2:
    dp[2] = [3, 2]
for i in range(4, N + 1, 2):
    dp[i][0] = dp[i - 2][0] * 3 + dp[i - 2][1]
    dp[i][1] = dp[i - 2][0] * 2 + dp[i - 2][1]
print(dp[N][0])