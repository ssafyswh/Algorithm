import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
level = [0] * (N + 1)
for _ in range(M):
    n, *order = map(int, input().split())
    for i in range(n - 1):
        a, b = order[i], order[i + 1]
        graph[a].append(b)
        level[b] += 1

q = deque([])
for i in range(1, N + 1):
    if level[i] == 0:
        q.append(i)

result = []
while q:
    num = q.popleft()
    for nxt in graph[num]:
        level[nxt] -= 1
        if level[nxt] == 0:
            q.append(nxt)
    result.append(num)

if len(result) == N:
    print('\n'.join(list(map(str, result))))
else:
    print(0)