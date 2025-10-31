import sys

T = int(input())
for _ in range(T):
    t = int(sys.stdin.readline())
    if t % 25 < 17:
        print('ONLINE')
    else:
        print('OFFLINE')