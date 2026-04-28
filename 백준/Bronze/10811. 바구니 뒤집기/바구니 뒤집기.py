N, M = map(int, input().split())
bucket = list(range(N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    temp = bucket[i: j + 1][::-1]
    for k in range(i, j + 1):
        bucket[k] = temp[k - i]
print(' '.join(list(map(str, bucket[1:]))))