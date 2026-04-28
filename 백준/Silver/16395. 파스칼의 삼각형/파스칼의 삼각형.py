n, k = map(int, input().split())
pascal = [[0] * N for N in range(n + 1)]
for i in range(1, n + 1):
    pascal[i][0] = 1
    pascal[i][-1] = 1
for i in range(2, n + 1):
    for j in range(1, i - 1):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
print(pascal[n][k - 1])