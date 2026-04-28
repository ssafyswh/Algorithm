from collections import deque

A, B = map(int, input().split())
route = deque([(A, 1)])
while route:
    now, count = route.popleft()
    if now == B:
        print(count)
        break
    if now * 2 <= B:
        route.append((now * 2, count + 1))
    if now * 10 + 1 <= B:
        route.append((now * 10 + 1, count + 1))
else:
    print(-1)