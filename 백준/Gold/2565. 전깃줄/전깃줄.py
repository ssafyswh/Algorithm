N = int(input())
codes = [() for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    codes[i] = (a, b)
codes.sort(key=lambda x: x[0])
result = [1] * N
for i in range(1, N):
    for j in range(i):
        if codes[i][1] > codes[j][1]:
            result[i] = max(result[i], result[j] + 1)
print(N - max(result))