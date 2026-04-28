import sys
N = int(input())
paint = [[0, 0, 0] for _ in range(N)]
paint[0] = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    R, G, B = list(map(int, sys.stdin.readline().split()))
    paint[i][0] = R + min(paint[i - 1][1], paint[i - 1][2])
    paint[i][1] = G + min(paint[i - 1][0], paint[i - 1][2])
    paint[i][2] = B + min(paint[i - 1][0], paint[i - 1][1])
print(min(paint[-1]))