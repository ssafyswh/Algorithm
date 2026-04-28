N = int(input())
cards = list(map(int, input().split()))
deck = [0] * 20000001
for card in cards:
    deck[card + 10000000] += 1
M = int(input())
targets = list(map(int, input().split()))
result = [0] * M
for i in range(M):
    result[i] = deck[targets[i] + 10000000]
print(*result)