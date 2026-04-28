import sys
from collections import deque


n = int(input())
family = [[] for _ in range(n + 1)]
checked = [0] * (n + 1)
one, two = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)
route = deque([one])
checked[one] = 1
result = 0
flag = False
while route:
    result += 1
    for _ in range(len(route)):
        now = route.popleft()
        for target in family[now]:
            if target == two:
                flag = True
                break
            if not checked[target]:
                checked[target] = 1
                route.append(target)
        if flag:
            break
    if flag:
        break
else:
    result = -1
print(result)