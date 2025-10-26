import sys
from heapq import heappop, heappush

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a].append((b, c))

MAX = float('inf')
start, goal = map(int, sys.stdin.readline().split())
distance = [MAX] * (n + 1)

hq = [(0, (start,))]
while hq:
    cost, route = heappop(hq)
    if distance[route[-1]] <= cost:
        continue
    if route[-1] == goal:
        print(cost)
        print(len(route))
        print(*route)
    distance[route[-1]] = cost
    route_unpack = list(route)
    for nxt, nxt_cost in bus[route[-1]]:
        if cost + nxt_cost >= distance[nxt]:
            continue
        route_unpack.append(nxt)
        heappush(hq, (cost + nxt_cost, tuple(route_unpack)))
        route_unpack.pop()