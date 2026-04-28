def horse(y=0, x=0, n=1, alps=None):
    if alps is None:
        alps = [maps[y][x]]
    global result
    for d in delta:
        dy, dx = y + d[0], x + d[1]
        if 0 <= dy < R and 0 <= dx < C:
            if maps[dy][dx] not in alps:
                alps.append(maps[dy][dx])
                if (dy, dx, tuple(alps)) not in memoization:
                    horse(dy, dx, n + 1, alps)
                    memoization.add((dy, dx, tuple(alps)))
                alps.pop()
    if n > result:
        result = n
    return


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
result = 0
memoization = set()
horse()
print(result)