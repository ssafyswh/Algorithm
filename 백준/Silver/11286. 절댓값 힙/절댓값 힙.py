import sys
import heapq

N = int(input())
q = []
for _ in range(N):
    command = int(sys.stdin.readline())
    if command:
        heapq.heappush(q, (abs(command), command // abs(command)))
    else:
        if q:
            value = heapq.heappop(q)
            print(value[0] * value[1])
        else:
            print(0)