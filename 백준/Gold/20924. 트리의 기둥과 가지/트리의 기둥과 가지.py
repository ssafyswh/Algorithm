import sys
from collections import deque

N, R = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a].append((b, d))
    tree[b].append((a, d))
now = R
stem = 0
visited = [False] * (N + 1)
while True:
    visited[now] = True
    temp_count = []
    temp_length = 0
    for target in tree[now]:
        if visited[target[0]]:
            continue
        temp_count.append(target[0])
        temp_length += target[1]
    if len(temp_count) == 1:
        stem += temp_length
        now = temp_count[0]
    else:
        giga = now
        break
longest = 0
branch = deque([(giga, 0)])
while branch:
    now, length = branch.popleft()
    visited[now] = True
    if longest < length:
        longest = length
    for target in tree[now]:
        if visited[target[0]]:
            continue
        branch.append((target[0], length + target[1]))

print(stem, longest)