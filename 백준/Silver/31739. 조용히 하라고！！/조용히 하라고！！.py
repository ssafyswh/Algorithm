import sys
input = sys.stdin.readline

N, M, K, T, P = map(int, input().split())
bugs = [list(map(int, input().split())) for _ in range(K)]

result = [0, 0]
caught = []

pos_dict = {}
for r, c, s in bugs:
    key = (r, c)
    pos_dict[key] = pos_dict.get(key, 0) + 1

mos = []
for (r, c), cnt in pos_dict.items():
    mos.append([r, c, cnt])

def oojeong(killK, nowT, y, x):
    if killK > result[0]:
        result[0] = killK
    if killK == K:
        return
    for i in range(len(mos)):
        if caught[i]:
            continue
        r, c, cnt = mos[i]
        dist = abs(y - r) + abs(x - c)
        if nowT >= dist:
            caught[i] = True
            oojeong(killK + cnt, nowT - dist, r, c)
            caught[i] = False

def areunm(y, x):
    value = 0
    for r, c, s in bugs:
        if y == r and x == c:
            value += 1
        else:
            dist = abs(y - r) + abs(x - c)
            if dist > 0 and P >= s * dist:
                value += 1
    if value > result[1]:
        result[1] = value

if mos:
    for i in range(len(mos)):
        caught = [False] * len(mos)
        caught[i] = True
        r, c, cnt = mos[i]
        oojeong(cnt, T, r, c)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        areunm(i, j)

print(*result)