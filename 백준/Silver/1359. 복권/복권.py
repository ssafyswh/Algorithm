def nCr(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    result = 1
    for i in range(1, r + 1):
        result = result * (n - r + i) // i
    return result

N, M, K = map(int, input().split())

num = 0
for t in range(K, M + 1):
    num += nCr(M, t) * nCr(N - M, M - t)

total = nCr(N, M)

print(num / total)