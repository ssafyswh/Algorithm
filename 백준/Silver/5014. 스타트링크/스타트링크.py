from collections import deque

floor, start, goal, up, down = map(int, input().split())

visited = [0] * (floor + 1)
route = deque([(start, 0)])
visited[start] = 1
count = 0
flag = False
if start != goal:
    while route:
        count += 1
        for _ in range(len(route)):
            now, button = route.popleft()
            if 0 < now - down <= floor and not visited[now - down]:
                if now - down == goal:
                    print(count)
                    flag = True
                    break
                visited[now - down] = 1
                route.append((now - down, count))

            if 0 < now + up <= floor and not visited[now + up]:
                if now + up == goal:
                    print(count)
                    flag = True
                    break
                visited[now + up] = 1
                route.append((now + up, count))
        if flag:
            break
    else:
        print('use the stairs')
else:
    print(count)