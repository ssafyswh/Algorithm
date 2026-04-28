N, M = list(map(int, input().split()))
A = []
B = []
for n in range(N):
    A.append(list(map(int, input().split())))
for n in range(N):
    B.append(list(map(int, input().split())))
for n in range(N):
    row = []
    for m in range(M):
        row.append(str(A[n][m] + B[n][m]))
    print(' '.join(row))