N, K = map(int, input().split())
time = list(map(int, input().split()))
result = 1
limit = time[0] + K
for i in range(1, N):
    if time[i] > limit:
        result += 1
        limit = time[i] + K
print(result)