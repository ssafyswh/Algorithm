import sys
import heapq

N, K = map(int, input().split())
bench = [[] for _ in range(12)]
team = [0] * 12

for _ in range(N):
    pi, wi = map(int, sys.stdin.readline().split())
    heapq.heappush(bench[pi], -wi)

for _ in range(K):
    for i in range(1, 12):
        if bench[i]:
            top = -bench[i][0]
            if top > team[i]:
                heapq.heappop(bench[i])
                if team[i] > 0:
                    heapq.heappush(bench[i], -team[i])
                team[i] = top
    for i in range(1, 12):
        team[i] = max(0, team[i] - 1)
    for i in range(1, 12):
        if bench[i]:
            top = -bench[i][0]
            if top > team[i]:
                heapq.heappop(bench[i])
                if team[i] > 0:
                    heapq.heappush(bench[i], -team[i])
                team[i] = top

print(sum(team))
