N, L = map(int, input().split())
a = list(map(int, input().split()))
result = 0
C = 0
for t in range(L):
    C += a[t]
    if 129 <= C <= 138:
        result += 1
for t in range(N - L):
    C = C - a[t] + a[t + L]
    if 129 <= C <= 138:
        result += 1

print(result)