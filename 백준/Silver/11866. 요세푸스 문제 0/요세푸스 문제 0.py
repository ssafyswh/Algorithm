N, K = map(int, input().split())
result = []
circle = list(range(1, N + 1))
remained = N
now = -1
for _ in range(N):
    now += K
    if now >= remained:
        now %= remained
    result.append(str(circle.pop(now)))
    now -= 1
    remained -= 1
print(f'<{", ".join(result)}>')