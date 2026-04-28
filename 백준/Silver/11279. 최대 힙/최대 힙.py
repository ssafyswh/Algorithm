import sys
import heapq
q = []
N = int(input())
for _ in range(N):
    command = int(sys.stdin.readline())
    if command:
        heapq.heappush(q, -command)
    else:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)