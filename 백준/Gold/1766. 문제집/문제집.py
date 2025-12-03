import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
level = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    level[b] += 1

q = []
for i in range(1, N + 1):
    if level[i] == 0:
        heappush(q, i)

result = []
while q:
    num = heappop(q)
    for nxt in graph[num]:
        level[nxt] -= 1
        if level[nxt] == 0:
            heappush(q, nxt)
    result.append(num)

print(*result)