import sys
input = sys.stdin.readline
from collections import deque

V = int(input())
tree = [[] for _ in range(V + 1)]
for _ in range(V):
    num, *edges, _ = map(int, input().split())
    for i in range(len(edges) // 2):
        tree[num].append((edges[i * 2], edges[i * 2 + 1]))

def dfs(t, start=1):
    far = 0
    value = 0
    visited = [False] * (V + 1)
    q = deque([(start, 0)])
    visited[start] = True
    while q:
        node, dist = q.popleft()
        if dist > value:
            value = dist
            far = node
        for nxt, nxt_dist in t[node]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            q.append((nxt, dist + nxt_dist))
    return far, value

node1, _ = dfs(tree)
print(dfs(tree, node1)[1])