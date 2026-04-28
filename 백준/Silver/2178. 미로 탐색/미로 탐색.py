from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
gy, gx = N - 1, M - 1
route = deque([(0, 0)])
maze[0][0] = 0
result = 1
flag = False
while route:
    result += 1
    for _ in range(len(route)):
        ny, nx = route.popleft()
        for d in delta:
            dy, dx = ny + d[0], nx + d[1]
            if [dy, dx] == [gy, gx]:
                flag = True
                break
            if 0 <= dy < N and 0 <= dx < M:
                if maze[dy][dx]:
                    route.append((dy, dx))
                    maze[dy][dx] = 0
        if flag:
            break
    if flag:
        break
print(result)