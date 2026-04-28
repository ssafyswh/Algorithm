import sys
from collections import deque

N, K = map(int, input().split())
result = [100000, 0]
visited = [False] * 100001
visited[N] = True
route = deque([(N, 0)])
while route:
    now, time = route.popleft()
    if time > result[0]:
        continue
    if now == K:
        if time < result[0]:
            result[0] = time
            result[1] = 1
        elif time == result[0]:
            result[1] += 1
        continue
    visited[now] = True
    if now * 2 <= 100000 and not visited[now * 2]:
        route.append((now * 2, time + 1))
    if now - 1 >= 0 and not visited[now - 1]:
        route.append((now - 1, time + 1))
    if now + 1 <= 100000 and not visited[now + 1]:
        route.append((now + 1, time + 1))
print(result[0])
print(result[1])