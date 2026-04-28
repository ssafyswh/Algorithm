from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
for i in range(N):
    route = deque([i])
    visited = [0] * N
    while route:
        now = route.popleft()
        for j in range(N):
            if visited[j] == 0 and graph[now][j] == 1:
                route.append(j)
                visited[j] = 1
                result[i][j] = 1
for row in result:
    print(' '.join(list(map(str, row))))