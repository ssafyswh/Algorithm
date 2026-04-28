N = int(input())
furu = list(map(int, input().split()))
fruit = [0] * 10
result, kind, count = 1, 1, 1
lower, upper = 0, 0
fruit[furu[lower]] = 1
while upper < N - 1:
    upper += 1
    if not fruit[furu[upper]]:
        kind += 1
    fruit[furu[upper]] += 1
    count += 1
    if kind > 2:
        while kind > 2:
            lower += 1
            count -= 1
            fruit[furu[lower - 1]] -= 1
            if fruit[furu[lower -1]] == 0:
                kind -= 1
    result = max(result, count)
print(result)