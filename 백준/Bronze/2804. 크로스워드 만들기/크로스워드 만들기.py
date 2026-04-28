A, B = input().split()
y, x = len(B), len(A)
crossword = [['.'] * x for _ in range(y)]
flag = False
for i in range(x):
    for j in range(y):
        if A[i] == B[j]:
            for a in range(y):
                crossword[a][i] = B[a]
            for b in range(x):
                crossword[j][b] = A[b]
            flag = True
            break
    if flag:
        break
for row in crossword:
    print(''.join(row))