import sys

R, C, Q = map(int, input().split())
picture = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
for y in range(R):
    for x in range(C):
        if x:
            picture[y][x] += picture[y][x-1]
        if y:
            picture[y][x] += picture[y-1][x]
        if x and y:
            picture[y][x] -= picture[y-1][x-1]
for _ in range(Q):
    r1, c1, r2, c2 = (x - 1 for x in map(int, sys.stdin.readline().split()))
    result = picture[r2][c2]
    if r1:
        result -= picture[r1-1][c2]
    if c1:
        result -= picture[r2][c1-1]
    if r1 and c1:
        result += picture[r1-1][c1-1]
    print(result // ((r2 - r1 + 1) * (c2 - c1 + 1)))