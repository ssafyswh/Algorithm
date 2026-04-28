def subset(s, n):
    if n == M:
        temp = []
        for i in range(N):
            if check[i] == 1:
                temp.append(i + 1)
        results.append(' '.join(list(map(str, temp))))
        return
    for i in range(s, N):
        if check[i] == 1:
            continue
        check[i] = 1
        subset(i + 1, n + 1)
        check[i] = 0


N, M = map(int, input().split())
series = list(range(1, N + 1))
check = [0] * N
results = []
subset(0, 0)
for result in results:
    print(result)