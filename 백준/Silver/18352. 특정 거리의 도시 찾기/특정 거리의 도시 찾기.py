import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
roads = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    roads[A].append(B)

results = []
q = deque([(X, 0)])
visited = [False] * (N + 1)
visited[X] = True
while q:
    now, distance = q.popleft()
    nxt_distance = distance + 1
    for target in roads[now]:
        if visited[target]:
            continue
        visited[target] = True
        if nxt_distance == K:
            results.append(target)
            continue
        q.append((target, nxt_distance))
if not results:
    print(-1)
else:
    results.sort()
    for result in results:
        print(result)