def subset(n):
    if n == M:
        print(' '.join(list(map(str, result))))
        return
    for i in range(N):
        if check[i] == 1:
            continue
        check[i] = 1
        result.append(i + 1)
        subset(n + 1)
        result.pop()
        check[i] = 0


N, M = map(int, input().split())
series = list(range(1, N + 1))
check = [0] * N
result = []
subset(0)