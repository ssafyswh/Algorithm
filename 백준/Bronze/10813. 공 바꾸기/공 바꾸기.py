N, M = list(map(int, input().split()))
bucket_list = list(range(1, N + 1))
for change in range(M):
    i, j = list(map(int, input().split()))
    bucket_list[i - 1], bucket_list[j - 1] = bucket_list[j - 1], bucket_list[i - 1]
print(' '.join(list(map(str, bucket_list))))