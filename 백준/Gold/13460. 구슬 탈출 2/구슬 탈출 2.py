from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move(sy, sx, direction):
    count = 0
    ny, nx = sy, sx
    dy, dx = delta[direction]
    while maps[ny + dy][nx + dx] != '#' and maps[ny][nx] != 'O':
        ny += dy
        nx += dx
        count += 1
    return ny, nx, count


def gravity(direction, red_start, blue_start):
    y_red, x_red = red_start
    y_blue, x_blue = blue_start
    dy, dx = delta[direction]

    ny_red, nx_red, count_red = move(y_red, x_red, direction)
    ny_blue, nx_blue, count_blue = move(y_blue, x_blue, direction)

    if (ny_red, nx_red) == (ny_blue, nx_blue) and maps[ny_red][nx_red] != 'O':
        if count_red > count_blue:
            ny_red -= dy
            nx_red -= dx
        else:
            ny_blue -= dy
            nx_blue -= dx
    return (ny_red, nx_red), (ny_blue, nx_blue)


def solve():
    q = deque([(red, blue, 0)])
    memoization = set((red, blue))
    while q:
        now_red, now_blue, turn = q.popleft()
        for d in range(4):
            d_red, d_blue = gravity(d, now_red, now_blue)
            if d_red == d_blue:
                continue
            if now_red == d_red and now_blue == d_blue:
                continue
            if maps[d_blue[0]][d_blue[1]] == 'O':
                continue
            if maps[d_red[0]][d_red[1]] == 'O':
                return turn + 1
            if (d_red, d_blue) in memoization:
                continue
            memoization.add((d_red, d_blue))
            if turn < 9:
                q.append((d_red, d_blue, turn + 1))

    return -1


N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]
for y in range(N):
    for x in range(M):
        if maps[y][x] == 'O':
            hole = (y, x)
        elif maps[y][x] == 'R':
            red = (y, x)
        elif maps[y][x] == 'B':
            blue = (y, x)

print(solve())