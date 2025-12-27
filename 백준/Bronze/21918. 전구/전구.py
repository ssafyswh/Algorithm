import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bulb = [0] + [*map(int, input().split())]
for _ in range(M):
    com, a, b = map(int, input().split())
    if com == 1:
        bulb[a] = b
    elif com == 2:
        for i in range(a, b + 1):
            if bulb[i] == 0:
                bulb[i] = 1
            else:
                bulb[i] = 0
    elif com == 3:
        for i in range(a, b + 1):
            bulb[i] = 0
    elif com == 4:
        for i in range(a, b + 1):
            bulb[i] = 1

print(*bulb[1:])