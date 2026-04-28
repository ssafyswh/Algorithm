time = [list(map(int, input().split())) for _ in range(12)]

groups = [(0,1), (2,3), (4,5), (6,7), (8,9), (10,11)]
INF = float('inf')
dp = [[INF, INF] for _ in range(6)]

a, b = groups[0]
dp[0][0] = time[b][a]
dp[0][1] = time[a][b]

for g in range(1, 6):
    prev_a, prev_b = groups[g - 1]
    a, b  = groups[g]
    for prev_state in (0, 1):
        prev_out = prev_a if prev_state == 0 else prev_b
        dp[g][0] = min(dp[g][0], dp[g-1][prev_state] + time[prev_out][b] + time[b][a])
        dp[g][1] = min(dp[g][1], dp[g-1][prev_state] + time[prev_out][a] + time[a][b])

print(min(dp[5][0], dp[5][1]))