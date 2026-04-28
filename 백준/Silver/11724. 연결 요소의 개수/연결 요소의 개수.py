from collections import deque

N, M =  map(int, input().split())
roads = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    roads[u].append(v)
    roads[v].append(u)
result = 0
for i in range(N):
    if visited[i] == 0:
        now = i
        route = deque([now])
        while route:
            now = route.pop()
            visited[now] = 1
            for j in roads[now]:
                if visited[j] == 0:
                    route.append(j)
        result += 1
print(result)