import sys

T = int(input())
for _ in range(T):
    n = int(input())
    a_sticker = list(map(int, sys.stdin.readline().split()))
    b_sticker = list(map(int, sys.stdin.readline().split()))
    x_sticker = [0] * n
    for i in range(1, n):
        a_sticker[i] += max(b_sticker[i - 1], x_sticker[i - 1])
        b_sticker[i] += max(a_sticker[i - 1], x_sticker[i - 1])
        x_sticker[i] += max(a_sticker[i - 1], b_sticker[i - 1])
    print(max(a_sticker[-1], b_sticker[-1], x_sticker[-1]))