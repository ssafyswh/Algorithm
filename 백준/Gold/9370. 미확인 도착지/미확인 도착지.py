import sys
import heapq

def dijkstra(start):
    dist = [MAX] * (n + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for nxt, wei in edges[now]:
            new_dist = distance + wei
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(q, (new_dist, nxt))
    return dist

T = int(input())
MAX = float('inf')
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n + 1)]
    s, g, h = map(int, sys.stdin.readline().split())
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        edges[a].append((b, d))
        edges[b].append((a, d))
    candidate = sorted([int(sys.stdin.readline()) for _ in range(t)])
    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    result = []
    s_g_h = dist_s[g] + dist_g[h]
    s_h_g = dist_s[h] + dist_h[g]
    for candy in candidate:
        if dist_s[candy] == MAX:
            continue
        if dist_s[candy] == s_g_h + dist_h[candy] or dist_s[candy] == s_h_g + dist_g[candy]:
            result.append(candy)
    print(*result)