N = int(input())
arr = list(map(int,input().split()))
result = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            result[i] = max(result[i], result[j] + 1)
print(max(result))
lis = []
cnt = max(result)
idx = N - 1
while cnt > 0 and idx >= 0:
    if result[idx] == cnt:
        lis.append(arr[idx])
        cnt -= 1
    idx -= 1
print(*(lis[::-1]))