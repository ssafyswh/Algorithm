import sys
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
maps = [list(sys.stdin.readline().strip('\n')) for _ in range(N)]
true_visited = [[0] * M for _ in range(N)]
false_visited = [[0] * M for _ in range(N)]
true_visited[0][0] = 1
route = deque([(0, 0, True)])
result = 1
flag = False
if N != 1 or M != 1:
    while route:
        result += 1
        for _ in range(len(route)):
            ny, nx, hammer = route.popleft()
            for d in delta:
                dy, dx = ny + d[0], nx + d[1]
                if dy == N - 1 and dx == M - 1:
                    flag = True
                    print(result)
                    break
                if 0 <= dy < N and 0 <= dx < M:
                    if hammer:
                        if not true_visited[dy][dx]:
                            if maps[dy][dx] == '1':
                                route.append((dy, dx, False))
                                false_visited[dy][dx] = 1
                            elif maps[dy][dx] == '0':
                                route.append((dy, dx, hammer))
                                true_visited[dy][dx] = 1
                    else:
                        if not true_visited[dy][dx] and not false_visited[dy][dx]:
                            if maps[dy][dx] == '0':
                                route.append((dy, dx, hammer))
                                false_visited[dy][dx] = 1

            if flag:
                break
        if flag:
            break
    else:
        print(-1)
else:
    print(1)