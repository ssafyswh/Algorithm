def series(n=0):
    if n == N:
        print(*result)
        return
    for i in range(1, N + 1):
        if selected[i]:
            continue
        selected[i] = True
        result.append(i)
        series(n + 1)
        result.pop()
        selected[i] = False

N = int(input())
selected = [False] * (N + 1)
result = []

series()