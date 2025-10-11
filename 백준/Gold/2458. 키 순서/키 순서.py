import sys
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

taller = [[False] * (N + 1) for _ in range(N + 1)]
for student in range(1, N + 1):
    q = deque([student])
    while q:
        now = q.popleft()
        for target in graph[now]:
            if taller[student][target]:
                continue
            taller[student][target] = True
            q.append(target)

result = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if taller[i][j]:
            count += 1
        elif taller[j][i]:
            count += 1
    if count == N - 1:
        result += 1
print(result)