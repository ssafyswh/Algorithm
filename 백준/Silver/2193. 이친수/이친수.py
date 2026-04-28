N = int(input())
if N < 2:
    result = 1
else:
    pinary = [[0, 0] for _ in range(N + 1)]
    pinary[1] = [0, 1]
    for i in range(2, N + 1):
        pinary[i][0] = sum(pinary[i - 1])
        pinary[i][1] = pinary[i - 1][0]
    result = sum(pinary[N])
print(result)