import sys
N, K = map(int, input().split())
backpack = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    for i in range(K, W - 1, -1):
        backpack[i] = max(backpack[i], backpack[i - W] + V)
print(backpack[K])