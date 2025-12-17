import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

f = [1, 2]
while f[-1] < 10**100:
    f.append(f[-1] + f[-2])

F = len(f)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
        
    lower = bisect_left(f, a)
    upper = bisect_right(f, b)
    print(upper - lower)