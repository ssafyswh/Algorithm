N = int(input())
A = list(map(int, input().split()))
result = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            result[i] = max(result[i], result[j] + 1)
print(max(result))