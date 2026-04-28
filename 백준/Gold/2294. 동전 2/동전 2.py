n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))
coins = list(coins)

MAX = 10001
dp = [MAX] * (k + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(-1 if dp[k] == MAX else dp[k])