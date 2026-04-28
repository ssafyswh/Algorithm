from collections import deque

import sys
N, M = map(int, input().split())
graph = [set() for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)
result = [N + 2, 0]  # number, count
for i in range(1, N + 1):
    kevin = deque([i])
    visited = [0] * (N + 1)
    visited[i] = -1
    count = 0
    while kevin:
        count += 1
        for _ in range(len(kevin)):
            now = kevin.popleft()
            for friend in graph[now]:
                if not visited[friend]:
                    visited[friend] = count
                    kevin.append(friend)
    temp = sum(visited) + 1
    if result[1] > temp or result[1] == 0:
        result = [i, temp]
    elif result[1] == temp:
        result[0] = min(result[0], i)
print(result[0])