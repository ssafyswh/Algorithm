import sys

N, M, K = map(int, sys.stdin.readline().split())
sand = [0] + list(map(int, sys.stdin.readline().split()))
rolling = list(map(int, sys.stdin.readline().split())) + [N + 1]
for i in range(1, N + 1):
    sand[i] += sand[i - 1]
sections = []
for i in range(K):
    cnt = (sand[rolling[i + 1] - 1] - sand[rolling[i] - 1])
    sections.append((cnt, i))

sections.sort(key=lambda x: (-x[0], x[1]))
result = []
for i in range(M):
    save, idx = sections[i]
    result.append(rolling[idx])
result.sort()
for i in range(M):
    print(result[i])
