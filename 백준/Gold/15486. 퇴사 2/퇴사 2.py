import sys
data = sys.stdin.read().split()

N = int(data[0])
dp = [0] * (N + 2)
idx = 1

for i in range(1, N + 1):
    t = int(data[idx])
    p = int(data[idx + 1])
    idx += 2

    if dp[i] < dp[i - 1]:
        dp[i] = dp[i - 1]
    if i + t <= N + 1 and dp[i + t] < dp[i] + p:
        dp[i + t] = dp[i] + p

print(max(dp[-1], dp[-2]))