import sys
from heapq import heappush, heappop

n, m = map(int, input().split())
courses = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
now = [0] * m
current = [0] * m
result = [0] * m

hq = []
for i in range(n):
    heappush(hq, (courses[i][0], i, 0))

now[0] = n
result[0] = n
time = 0

while hq:
    now_total, entry_num, now_range = heappop(hq)

    if time != now_total:
        for r in range(m):
            if current[r]:
                now[r] += current[r]
                result[r] = max(result[r], now[r])
                current[r] = 0
        time = now_total
    current[now_range] -= 1

    if now_range == m - 1:
        continue

    nxt_range = now_range + 1
    current[nxt_range] += 1
    heappush(hq,(now_total + courses[entry_num][nxt_range], entry_num, nxt_range))

for r in range(m):
    if current[r]:
        now[r] += current[r]
        result[r] = max(result[r], now[r])
        current[r] = 0

print(*result)