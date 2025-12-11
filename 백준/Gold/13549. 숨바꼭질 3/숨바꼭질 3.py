from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001
route = deque([(N, 0)])
if N != K:
    while route:
        now, time = route.popleft()
        if now == K:
            print(time)
            break
        if now * 2 <= 100000 and not visited[now * 2]:
            route.append((now * 2, time))
            visited[now * 2] = 1
        if now - 1 >= 0 and not visited[now - 1]:
            route.append((now - 1, time + 1))
            visited[now - 1] = 1
        if now + 1 <= 100000 and not visited[now + 1]:
            route.append((now + 1, time + 1))
            visited[now + 1] = 1
else:
    print(0)