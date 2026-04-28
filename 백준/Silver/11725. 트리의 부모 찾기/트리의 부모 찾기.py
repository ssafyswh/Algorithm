import sys
from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    tree[B].append(A)
    tree[A].append(B)
parent = [0] * (N + 1)
route = deque([1])
parent[1] = 1
while route:
    now = route.popleft()
    for target in tree[now]:
        if not parent[target]:
            route.append(target)
            parent[target] = now

for i in range(2, N + 1):
    print(parent[i])