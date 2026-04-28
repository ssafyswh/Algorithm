import sys

Q = int(input())
k = 0.00176
for _ in range(Q):
    a, m = map(int, sys.stdin.readline().split())
    result = a * m * k
    print(int(result))