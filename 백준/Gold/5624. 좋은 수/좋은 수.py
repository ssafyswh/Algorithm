import sys
input = sys.stdin.readline

N = int(input())
A = [*(map(int, input().split()))]

result = 0
limit = 2 * 10 ** 5
dp = [0] * (2 * limit + 1)

for i in range(1, N):
    for j in range(i - 1, -1, -1):
        temp_sum = A[i - 1] + A[j]
        dp[temp_sum + limit] = 1

    for j in range(i - 1, -1, -1):
        temp_diff = A[i] - A[j]
        if dp[temp_diff + limit] == 1:
            result += 1
            break

print(result)