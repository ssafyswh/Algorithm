n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
def check_coffee(y, x):
    for d in delta:
        dy, dx = y + d[0], x + d[1]
        if not (0 <= dy < n and 0 <= dx < m):
            continue
        if maps[dy][dx] == 'E':
            return False

    return True


for y in range(n):
    for x in range(m):
        if maps[y][x] == '#':
            continue
        if check_coffee(y, x):
            maps[y][x] = 'E'

for row in maps:
    print(''.join(row))