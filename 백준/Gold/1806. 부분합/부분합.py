N, S = map(int, input().split())
series = list(map(int, input().split()))

start, end = 0, 0
now_sum = 0
result = N + 1
while True:
    if now_sum >= S:
        result = min(result, end - start)
        now_sum -= series[start]
        start += 1
    elif end == N:
        break
    else:
        now_sum += series[end]
        end += 1

print(0 if result == N + 1 else result)