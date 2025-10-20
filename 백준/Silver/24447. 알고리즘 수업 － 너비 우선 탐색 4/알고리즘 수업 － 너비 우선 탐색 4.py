import sys
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for edges in graph:
    edges.sort()
depth = [-1] * (N + 1)
order = [0] * (N + 1)
visited = [False] * (N + 1)
depth[R] = 0
order[R] = 1
visited[R] = True
q = deque([R])
now_order = 1
while q:
    now = q.popleft()
    nxt_depth = depth[now] + 1
    for target in graph[now]:
        if visited[target]:
            continue
        visited[target] = True
        q.append(target)
        depth[target] = nxt_depth
        now_order += 1
        order[target] = now_order


print(sum(order[i] * depth[i] for i in range(1, N + 1)))