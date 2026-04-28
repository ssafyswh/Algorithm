def turn(n):
    if n < 3:
        return n + 1
    return 0

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

C, R = map(int, input().split())
K = int(input())
if C * R < K:
    result = [0]
else:
    count = 0
    seat = [[0] * C for _ in range(R)]
    y, x = (-1, 0)
    direct = 0
    d = delta[direct]
    while count < C * R:
        count += 1
        if not (0 <= y + d[0] < R and 0 <= x + d[1] < C) or seat[y + d[0]][x + d[1]]:
            direct = turn(direct)
        d = delta[direct]
        y, x = y + d[0], x + d[1]
        seat[y][x] = count
        if count == K:
            result = [x + 1, y + 1]

print(*result)
