n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
coins = []

for _ in range(n):
    coins.append(int(input()))
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]
print(dp[k])