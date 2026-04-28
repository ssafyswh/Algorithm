import sys
N, M, B = map(int, input().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
low = 256
high = 0
count = [0] * 257
for y in range(N):
    for x in range(M):
        value = land[y][x]
        count[value] += 1
        low = min(low, value)
        high = max(high, value)
result = [128000001, 0]
for height in range(low, high + 1):
    time = 0
    bag = B
    for i in range(257):
        if i > height:
            time += 2 * count[i] * (i - height)
            bag += count[i] * (i - height)
        elif i < height:
            time += count[i] * (height - i)
            bag -= count[i] * (height - i)
    if bag < 0:
        continue
    if result[0] > time:
        result = [time, height]
    elif result[0] == time:
        result[1] = max(height, result[1])
print(*result)