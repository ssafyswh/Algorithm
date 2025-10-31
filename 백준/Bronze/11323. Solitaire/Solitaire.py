import sys

T = int(input())
for _ in range(T):
    N = int(input())
    dice = list(map(int, sys.stdin.readline().split()))
    S = 0
    now = 0
    count = -1
    while True:
        count += 1
        if now + dice[count % 6] <= N:
            now += dice[count % 6]
            S += now
        if now == N:
            break
    print(S)