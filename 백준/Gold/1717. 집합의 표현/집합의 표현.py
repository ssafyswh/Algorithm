import sys
sys.setrecursionlimit(10**6)
def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_a, node_b):
    A = find(node_a)
    B = find(node_b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B

n, m = map(int, input().split())
parent = list(range(n + 1))
for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union(a, b)
    elif command == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')