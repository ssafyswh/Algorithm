from collections import deque

N = int(input())
visited = [0] * (N + 1)
compute = deque([N])
result = 0
flag = False
while N > 1:
    result += 1
    for _ in range(len(compute)):
        now = compute.popleft()
        if not now % 3 and not visited[now // 3]:
            if now // 3 == 1:
                flag = True
                break
            compute.append(now // 3)
            visited[now // 3] = 1
        if not now % 2 and not visited[now // 2]:
            if now // 2 == 1:
                flag = True
                break
            compute.append(now // 2)
            visited[now // 2] = 1
        if now - 1:
            if not visited[now - 1]:
                compute.append(now - 1)
                visited[now - 1] = 1
        else:
            flag = True
            break
    if flag:
        break
print(result)