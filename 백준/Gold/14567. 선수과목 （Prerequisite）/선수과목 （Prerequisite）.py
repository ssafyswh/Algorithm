import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
prerequisite = [0] * (N + 1)
subjects = [[] for _ in range(N + 1)]


for _ in range(M):
    a, b = map(int, input().split())
    prerequisite[b] += 1
    subjects[a].append(b)

result = [0] * (N + 1)
q = deque([])
for i in range(1, N + 1):
    if prerequisite[i] == 0:
        q.append(i)

semester = 0
while q:
    semester += 1
    for _ in range(len(q)):
        now = q.popleft()
        for target in subjects[now]:
            prerequisite[target] -= 1
            if prerequisite[target] == 0:
                q.append(target)
        result[now] = semester
print(*result[1:])