import sys

def Euclidean(a, b):
    if b == 0:
        return a
    return Euclidean(b, a % b)

N = int(input())
tree = [int(sys.stdin.readline()) for _ in range(N)]
dist = [tree[x + 1] - tree[x] for x in range(N - 1)]
gcd = dist[0]
for i in range(1, N - 1):
    gcd = Euclidean(gcd, dist[i])
    if gcd == 1:
        break
result = 0
for i in range(N - 1):
    result += (dist[i] // gcd) - 1
print(result)