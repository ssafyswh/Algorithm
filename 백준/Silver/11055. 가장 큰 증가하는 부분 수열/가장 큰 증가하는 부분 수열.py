N = int(input())
A = list(map(int, input().split()))

result = A[:]
for i in range(N):
    num = A[i]
    for j in range(i):
        if num > A[j]:
            result[i] = max(result[i], result[j] + num)

print(max(result))