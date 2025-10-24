import sys
import heapq

hq = []
while True:
    register = sys.stdin.readline().split()
    if register[0] == '#':
        break
    q_num, period = map(int, register[1:])
    heapq.heappush(hq, (period, q_num, period))

K = int(input())
for _ in range(K):
    time, q_num, period = heapq.heappop(hq)
    print(q_num)
    heapq.heappush(hq, (time + period, q_num, period))