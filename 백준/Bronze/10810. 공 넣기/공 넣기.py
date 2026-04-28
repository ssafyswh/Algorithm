N, M = list(map(int, input().split()))
bucket_list = [0] * N
for _ in range(M):
    i, j, k = list(map(int, input().split()))
    for idx in range(len(bucket_list[i - 1 : j])):
        bucket_list[idx + i - 1] = k
print(' '.join(list(map(str, bucket_list)))) 