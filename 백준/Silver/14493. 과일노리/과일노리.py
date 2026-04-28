import sys

N = int(input())
time = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    bot = time % (a + b)
    if bot < b:
        time += b - bot
    time += 1
print(time)