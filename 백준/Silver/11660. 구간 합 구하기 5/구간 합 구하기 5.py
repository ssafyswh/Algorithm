import sys

N, M = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for x in range(N):
    for y in range(N):
        temp = matrix[x][y]
        if x:
            temp += matrix[x - 1][y]
        if y:
            temp += matrix[x][y - 1]
        if x and y:
            temp -= matrix[x - 1][y - 1]
        matrix[x][y] = temp
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    result = matrix[x2][y2]
    if x1:
        result -= matrix[x1- 1][y2]
    if y1:
        result -= matrix[x2][y1 - 1]
    if x1 and y1:
        result += matrix[x1 - 1][y1 - 1]
    print(result)
