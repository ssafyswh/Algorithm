N = int(input())
cards = set(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

result = [0] * M
for i in range(M):
    if targets[i] in cards:
        result[i] = 1
print(' '.join(list(map(str, result))))