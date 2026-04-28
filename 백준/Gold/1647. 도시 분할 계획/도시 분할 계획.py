import sys
import heapq


N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((c, b))
    edges[b].append((c, a))
q = []
result = 0
count = 0
visited = [False] * (N + 1)
now = 1
visited[1] = True
for target in edges[1]:
    heapq.heappush(q, (target[0], target[1]))
longest = 0
while count < N - 1:
    cost, node = heapq.heappop(q)
    if visited[node]:
        continue
    visited[node] = True
    result += cost
    longest = max(longest, cost)
    count += 1
    for nxt_cost, nxt in edges[node]:
        if not visited[nxt]:
            heapq.heappush(q, (nxt_cost, nxt))
print(result - longest)