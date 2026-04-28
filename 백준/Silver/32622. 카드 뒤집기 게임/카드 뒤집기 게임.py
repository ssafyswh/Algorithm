import sys

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
result = [1]
for i in range(1, N):
    if card[i] != card[i - 1]:
        result.append(1)
    else:
        result[-1] += 1
for j in range(len(result) - 1, 0, -1):
    result[j] += result[j - 1]
print(max(result))