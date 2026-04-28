from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
R, C = map(int, input().split())

forest = [list(input()) for _ in range(R)]
water = []
for y in range(R):
    for x in range(C):
        if forest[y][x] == 'S':
            sy, sx = y, x
        elif forest[y][x] == '*':
            water.append((y, x))
hedgehog = deque([(sy, sx)])
visited = [[0] * C for _ in range(R)]
visited[sy][sx] = 1
flood = deque(water)
count = 0
flag = False
while hedgehog:
    count += 1
    for _ in range(len(flood)):
        fy, fx = flood.popleft()
        for d in delta:
            dfy, dfx = fy + d[0], fx + d[1]
            if 0 <= dfy < R and 0 <= dfx < C:
                if forest[dfy][dfx] == '.' or forest[dfy][dfx] == 'S':
                    flood.append((dfy, dfx))
                    forest[dfy][dfx] = '*'
    for _ in range(len(hedgehog)):
        hy, hx = hedgehog.popleft()
        for d in delta:
            dhy, dhx = hy + d[0], hx + d[1]
            if 0 <= dhy < R and 0 <= dhx < C and not visited[dhy][dhx]:
                if forest[dhy][dhx] == 'D':
                    flag = True
                    break
                elif forest[dhy][dhx] == '.':
                    hedgehog.append((dhy, dhx))
                    visited[dhy][dhx] = 1
        if flag:
            break
    if flag:
        print(count)
        break
else:
    print('KAKTUS')