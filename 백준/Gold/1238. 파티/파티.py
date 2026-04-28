import sys
import heapq


N, M, X = map(int, input().split())
go_party = [[] for _ in range(N + 1)]
back_home = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    go_party[end].append((start, time))
    back_home[start].append((end, time))
result = [0] * (N + 1)
q1 = [(0, X)]
visited = [False] * (N + 1)
while q1:
    distance, now = heapq.heappop(q1)
    if visited[now]:
        continue
    visited[now] = True
    result[now] = distance
    for target in back_home[now]:
        if visited[target[0]]:
            continue
        heapq.heappush(q1, (distance + target[1], target[0]))
q2 = [(0, X)]
visited = [False] * (N + 1)
while q2:
    distance, now = heapq.heappop(q2)
    if visited[now]:
        continue
    visited[now] = True
    result[now] += distance
    for target in go_party[now]:
        if visited[target[0]]:
            continue
        heapq.heappush(q2, (distance + target[1], target[0]))
print(max(result))
