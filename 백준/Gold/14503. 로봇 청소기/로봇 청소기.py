def rotate():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1
    return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
room = [list(map(int, input().split())) for _ in range(N)]
now_y = r
now_x = c
result = 0
while True:
    if room[now_y][now_x] == 0:
        result += 1
        room[now_y][now_x] = -1
    for dl in delta:
        dy = now_y + dl[0]
        dx = now_x + dl[1]
        if 0 <= dy < N and 0 <= dx < M:
            if room[dy][dx] == 0:
                break
    else:
        dy = now_y - delta[d][0]
        dx = now_x - delta[d][1]
        if 0 <= dy < N and 0 <= dx < M:
            if room[dy][dx] != 1:
                now_y = dy
                now_x = dx
                continue
            else:
                break
        else:
            break
    while True:
        rotate()
        dy = now_y + delta[d][0]
        dx = now_x + delta[d][1]
        if 0 <= dy < N and 0 <= dx < M:
            if room[dy][dx] == 0:
                now_y = dy
                now_x = dx
                break
print(result)