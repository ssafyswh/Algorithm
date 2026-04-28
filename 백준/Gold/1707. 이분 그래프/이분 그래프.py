import sys
from collections import deque


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    vertex = [0] * (V + 1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    flag = False
    for i in range(1, 1 + V):
        if not vertex[i]:
            paint = deque([i])
            vertex[i] = 1
            while paint:
                now = paint.popleft()
                for target in graph[now]:
                    if vertex[target] and vertex[target] == vertex[now]:
                        print('NO')
                        flag = True
                        break
                    elif not vertex[target]:
                        vertex[target] = -vertex[now]
                        paint.append(target)
                if flag:
                    break
            if flag:
                break
    else:
        print('YES')