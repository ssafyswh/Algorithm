N = int(input())
dp = [5] * (N + 1)
for i in range(1, N + 1):
    if (i ** 0.5) % 1 == 0:
        dp[i] = 1
    else:
        j = int(i ** 0.5)
        while True:
            if j < 1:
                break
            dp[i] = min(dp[i], 1 + dp[i - j * j])
            if dp[i] == 2:
                break
            j -= 1
print(dp[-1])