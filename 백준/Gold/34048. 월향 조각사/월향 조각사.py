import sys

N = int(input())
marbles = list(map(int, sys.stdin.readline().split()))


dp_left = [0] * N
dp_right = [0] * N
dp_left[0] = 1
dp_right[-1] = 1

for i in range(1, N):
    dp_left[i] = min(dp_left[i - 1] + 1, marbles[i])
for i in range(N - 2, -1, -1):
    dp_right[i] = min(dp_right[i + 1] + 1, marbles[i])

result = 0
for i in range(N):
    result += min(dp_left[i], dp_right[i])

print(result)