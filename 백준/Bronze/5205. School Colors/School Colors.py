import sys
input = sys.stdin.readline

K = int(input())
for case_num in range(1, 1 + K):
    N = int(input())
    colors = [[*map(int, input().split())] for _ in range(N)]

    results = []
    value = 0

    for i in range(N):
        ri, gi, bi = colors[i]
        for j in range(i + 1, N):
            rj, gj, bj = colors[j]
            contrast = ((ri - rj) ** 2 + (gi - gj) ** 2 + (bi - bj) ** 2) ** 0.5
            if contrast > value:
                value = contrast
                results = [(i + 1, j + 1)]
            elif contrast == value:
                results.append((i + 1, j + 1))

    print(f'Data Set {case_num}:')
    for result in results:
        print(*result)