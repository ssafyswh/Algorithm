import sys

N = int(input())
book = list(map(int, sys.stdin.readline().split()))
book.sort()
result = 1
now = book[0]
for i in range(1, N):
    if book[i] >= now * 2:
        result += 1
        now = book[i]
print(result)