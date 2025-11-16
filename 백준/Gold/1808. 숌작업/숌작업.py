import sys

def set_level(node, h):
    levels[node] = h
    for child in children[node]:
        set_level(child, h + 1)
    return

def works(p_node, c_node):
    children[p_node].add(c_node)
    children[parents[c_node]].remove(c_node)
    parents[c_node] = p_node
    gap = levels[c_node] - levels[p_node] - 1
    set_level(p_node, levels[p_node])
    return gap

def solve(limit_h):
    cnt = 0
    while True:
        target = levels.index(max(levels))
        if levels[target] > limit_h:
            gap = levels[target] - limit_h
            c_node = target
            h = min(2, limit_h + 1)
            while levels[c_node] > h:
                c_node = parents[c_node]

            if levels[c_node] > limit_h:
                p_node = c_node
                for _ in range(gap+1):
                    p_node = parents[p_node]
            else:
                p_node = 0
            cnt += works(p_node,c_node)
        else:
            return cnt

N = int(input())
parents = [0] * N
children = [set() for _ in range(N)]
levels = [0] * N
for _ in range(N - 1):
    a,b = map(int, sys.stdin.readline().split())
    parents[b] = a
    children[a].add(b)
set_level(0, 0)
H = int(input())
result = solve(H)
print(result)