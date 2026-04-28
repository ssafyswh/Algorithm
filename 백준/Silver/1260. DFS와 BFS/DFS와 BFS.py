from collections import deque


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N + 1):
    graph[i].sort()
visited = [0] * (N + 1)
visited[V] = 1
result1 = [V]
route = [V]
while route:
    now = route[-1]
    if graph[now]:
        for target in graph[now]:
            if not visited[target]:
                route.append(target)
                result1.append(target)
                visited[target] = 1
                break
        else:
            route.pop()
    else:
        route.pop()
print(*result1)
visited = [0] * (N + 1)
route = deque([V])
visited[V] = 1
result2 = [V]
while route:
    for _ in range(len(route)):
        now = route.popleft()
        for target in graph[now]:
            if not visited[target]:
                route.append(target)
                result2.append(target)
                visited[target] = 1
print(*result2)