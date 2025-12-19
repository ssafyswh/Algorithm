import sys
input = sys.stdin.readline

def multi(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def power(A, n):
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            res = multi(res, A)
        A = multi(A, A)
        n //= 2
    return res

N = int(input())
mod = 10 ** 9 + 7
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    f = [[1, 1], [1, 0]]
    result = power(f, N)
    print(result[0][1])