import sys

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    wall = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    for y in range(n):
        cnt = 0
        for x in range(m):
            if wall[y][x] == 0:
                cnt = 0
                continue
            cnt += 1
            if cnt > k:
                print('NO')
                return
            wall[y][x] = (x + y) % k + 1

    for x in range(m):
        cnt = 0
        for y in range(n):
            if wall[y][x] == 0:
                cnt = 0
                continue
            cnt += 1
            if cnt > k:
                print('NO')
                return
            wall[y][x] = (x + y) % k + 1
    print('YES')
    for row in wall:
        print(*row)

T = int(input())
for _ in range(T):
    solve()