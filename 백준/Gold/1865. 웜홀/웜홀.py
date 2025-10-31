import sys

def BF(st=1):
    distance = [MAX] * (N + 1)
    distance[st] = 0
    for i in range(N):
        for start, end, weight in wormhole:
            nxt_dist = distance[start] + weight
            if distance[end] > nxt_dist:
                distance[end] = nxt_dist
                if i == N - 1:
                    # 음수 사이클이 존재한다.
                    return True
    # 음수 사이클이 존재하지 않는다.
    return False

MAX = 250000000

T = int(input())
for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    wormhole = []
    for _ in range(M):
        s, e, t = map(int ,sys.stdin.readline().split())
        wormhole.append((s, e, t))
        wormhole.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, sys.stdin.readline().split())
        wormhole.append((s, e, -t))
    if BF():
        print('YES')
    else:
        print('NO')