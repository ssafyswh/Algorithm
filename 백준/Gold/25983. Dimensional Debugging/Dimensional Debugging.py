import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
algos = []
q = deque([])
result = [0] * N

for i in range(N):
    L = list(map(int, input().split()))
    H = list(map(int, input().split()))
    algos.append((L, H))
    if all(x == 0 for x in L):
        q.append(i)
        result[i] = 1

while q:
    now = q.popleft()
    L_now, H_now = algos[now]
    for i in range(N):
        if result[i]:
            continue
        L_i, H_i = algos[i]
        check = True
        for k in range(K):
            if L_i[k] > H_now[k]:
                check = False
                break
        if check:
            result[i] = 1
            q.append(i)

print(sum(result))