import sys
input = sys.stdin.readline

N = int(input())
coin = [*map(int, input().split())]

cheapest = coin[0]
result = 0

for i in range(1, N):
    if coin[i] > cheapest:
        result = max(result, coin[i] - cheapest)
    if coin[i] < cheapest:
        cheapest = coin[i]

print(result)