import sys

N = int(input())
result = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    result.append((x, y))
result.sort()
for index in result:
    print(index[0], index[1])