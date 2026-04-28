from collections import deque

N = int(input())
M = int(input())
network = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
result = 0
route = deque([1])
while route:
    now = route.popleft()
    visited[now] = 1
    for node in network[now]:
        if not visited[node]:
            route.append(node)
            visited[node] = 1
            result += 1
print(result)