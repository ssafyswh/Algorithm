import sys

n = int(input())
wine = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    goblet = int(sys.stdin.readline())
    if i == 0:
        wine[0][0] = goblet
        continue
    elif i == 1:
        wine[1][0] = goblet
        wine[1][1] = goblet + wine[0][0]
        continue
    wine[i][0] = goblet + max(wine[i - 2])
    wine[i][1] = goblet + wine[i - 1][0]
    wine[i][2] = max(wine[i - 1])
print(max(wine[n - 1]))