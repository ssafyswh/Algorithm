import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0] * 21 for _ in range(N - 1)]
dp[0][nums[0]] = 1
for i in range(1, N - 1):
    num = nums[i]
    for j in range(21):
        if j - num >= 0:
            dp[i][j] += dp[i - 1][j - num]
        if j + num <= 20:
            dp[i][j] += dp[i - 1][j + num]
print(dp[N - 2][nums[N - 1]])