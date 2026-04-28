def subset(n):
    if n == M:
        results.append(' '.join(list(map(str, result))))
        return
    for i in range(N):
        check[i] += 1
        result.append(i + 1)
        subset(n + 1)
        check[i] -= 1
        result.pop()


N, M = map(int, input().split())
series = list(range(1, N + 1))
check = [0] * N
result = []
results = []
subset(0)
for result in results:
    print(result)