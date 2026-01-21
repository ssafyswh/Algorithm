import sys
input = sys.stdin.readline

N = int(input())
# 2^16 > 50000
LOG = 16

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

# ancestors[k][node]: node의 2^k번째 조상
ancestors = [[0] * (N + 1) for _ in range(LOG)]
depth = [-1] * (N + 1)

def fill_depth():
    stack = [(1, 0)]
    depth[1] = 0
    while stack:
        now, d = stack.pop()
        for nxt in tree[now]:
            if depth[nxt] != -1:
                continue
            ancestors[0][nxt] = now
            depth[nxt] = d + 1
            stack.append((nxt, d + 1))

fill_depth()

for i in range(1, LOG):
    for j in range(1, N + 1):
        prev_ancestor = ancestors[i - 1][j]
        if prev_ancestor != 0:
            ancestors[i][j] = ancestors[i - 1][prev_ancestor]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    diff = depth[b] - depth[a]
    for i in range(LOG):
        if (diff >> i) & 1:
            b = ancestors[i][b]

    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        if ancestors[i][a] != ancestors[i][b]:
            a = ancestors[i][a]
            b = ancestors[i][b]

    return ancestors[0][a]

M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
