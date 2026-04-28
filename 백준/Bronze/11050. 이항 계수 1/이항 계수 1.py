def f(n):
    if n <= 1:
        return 1
    return n * f(n-1)

N, K = map(int, input().split())
result = f(N) // (f(K) * f(N-K))
print(result)