def subset(l, s, n):
    if n == M:
        print(' '.join(list(map(str, l))))
        return
    for i in range(s, N + 1):
        l.append(i)
        subset(l, i, n + 1)
        l.pop()


N, M = map(int, input().split())
results = []
subset([], 1, 0)