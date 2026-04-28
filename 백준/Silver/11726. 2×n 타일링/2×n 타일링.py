N = int(input())
result = [1, 2, 3]
if N <= 3:
    print(result[N - 1])
else:
    for _ in range(N - 3):
        result = [result[1], result[2], result[1] + result[2]]
    print(result[2] % 10007)