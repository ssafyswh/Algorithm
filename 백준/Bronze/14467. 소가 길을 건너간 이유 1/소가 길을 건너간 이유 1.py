import sys
input = sys.stdin.readline

N = int(input())
cow = dict()
result = 0
for _ in range(N):
    c, d = map(int, input().split())
    if cow.get(c) is None:
        cow[c] = d
    elif cow[c] != d:
        result += 1
        cow[c] = d
print(result)