import sys
input = sys.stdin.readline

N = int(input())
consults = [(0, 0)]
for _ in range(N):
    t, p = map(int, input().split())
    consults.append((t, p))

result = [0] * (N + 2)
for i in range(1, N + 1):
    time, price = consults[i]
    result[i] = max(result[i], result[i - 1])
    if i + time < N + 2:
        result[i + time] = max(result[i + time], result[i] + price)

result[-1] = max(result[-1], result[-2])
print(result[-1])