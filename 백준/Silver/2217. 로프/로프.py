import sys
input = sys.stdin.readline

N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()
result = 0
for i in range(N):
    result = max(result, rope[i] * (N - i))
print(result)