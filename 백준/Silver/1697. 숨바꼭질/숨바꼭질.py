from collections import deque

N, K = map(int, input().split())
route = deque([N])
visited = [0] * 100001
result = 0
flag = False
if N != K:
    while route:
        result += 1
        for _ in range(len(route)):
            now = route.popleft()
            visited[now] = 1
            if now > 0 and not visited[now - 1]:
                if now - 1 == K:
                    flag = True
                    break
                route.append(now - 1)
                visited[now - 1] = 1
            if now < 100000 and not visited[now + 1]:
                if now + 1 == K:
                    flag = True
                    break
                route.append(now + 1)
                visited[now + 1] = 1
            if now * 2 <= 100000 and not visited[now * 2]:
                if now * 2 == K:
                    flag = True
                    break
                route.append(now * 2)
                visited[now * 2] = 1
        if flag:
            break
print(result)