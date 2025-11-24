d, start = input().split()
d = int(d)

words = [start]
for _ in range(d):
    words.append(input().strip())

words = list(set(words))
words.sort(key=len)

index = {w: i for i, w in enumerate(words)}
n = len(words)
adj = [[] for _ in range(n)]

def can_transform(a, b):
    if len(b) != len(a) + 1:
        return False
    i = j = diff = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            diff += 1
            j += 1
            if diff > 1:
                return False
    return True

for i in range(n):
    for j in range(i+1, n):
        if len(words[j]) == len(words[i]) + 1:
            if can_transform(words[i], words[j]):
                adj[i].append(j)

dp = [''] * n
dp[index[start]] = start

for i in range(n):
    if dp[i] == '':
        continue
    for nxt in adj[i]:
        if len(dp[nxt]) < len(dp[i]) + (len(words[nxt]) - len(words[i])):
            dp[nxt] = words[nxt]

result = max(dp, key=len)
print(result)