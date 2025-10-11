import sys

R, C = map(int, input().split())
image = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
J = [[0] * (C - 2) for _ in range(R - 2)]
T = int(input())
result = 0
for y in range(R - 2):
    for x in range(C - 2):
        filt = []
        for dy in range(3):
            for dx in range(3):
                filt.append(image[y + dy][x + dx])
        filt.sort()
        if filt[4] >= T:
            result += 1
print(result)