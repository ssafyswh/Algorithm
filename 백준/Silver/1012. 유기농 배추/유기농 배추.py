import sys
from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [0] * (M * N)
    cabbage = [0] * K
    visited = [0] * (N * M)
    delta1 = [-1, 1]
    delta2 = [-M, M]
    result = 0
    for k in range(K):
        X, Y =  map(int, sys.stdin.readline().split())
        farm[X + Y * M] = 1
        cabbage[k] = X + Y * M
    for i in range(K):
        if not visited[cabbage[i]]:
            route = deque([cabbage[i]])
            visited[cabbage[i]] = 1
            while route:
                now = route.popleft()
                for d in delta1:
                    if (d == -1 and now % M == 0) or (d == 1 and now % M == M - 1):
                        continue
                    else:
                        dn = d + now
                        if not visited[dn]:
                            visited[dn] = 1
                            if farm[dn]:
                                route.append(dn)
                for d in delta2:
                    dn = d + now
                    if 0 <= dn < M * N and not visited[dn]:
                        visited[dn] = 1
                        if farm[dn]:
                            route.append(dn)
            result += 1
    print(result)