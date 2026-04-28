N = int(input())
sequence = list(map(int, input().split()))
result = 0
count = 0
for i in range(N):
    if not count:
        count = 1
    elif sequence[i] >= sequence[i - 1]:
        count += 1
    else:
        result = max(result, count)
        count = 1
result = max(result, count)
count = 0
for i in range(N):
    if not count:
        count = 1
    elif sequence[i] <= sequence[i - 1]:
        count += 1
    else:
        result = max(result, count)
        count = 1
result = max(result, count)
print(result)