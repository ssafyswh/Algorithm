def find_leaf(n):
    global result
    if not child[n]:
        result += 1
        return
    for m in child[n]:
        find_leaf(m)


N = int(input())
parent = list(map(int, input().split()))
for i in range(N):
    if parent[i] == -1:
        root = i
        break
delete = int(input())
if root == delete:
    result = 0
else:
    parent[delete] = -1
    child = [[] for _ in range(N)]
    for i in range(N):
        if parent[i] != -1:
            child[parent[i]].append(i)
    child[delete] = []
    result = 0
    find_leaf(root)
print(result)