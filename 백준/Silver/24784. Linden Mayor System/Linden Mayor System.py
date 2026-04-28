from collections import deque

n, m = map(int, input().split())
rules = {}
for _ in range(n):
    x, y = input().split(' -> ')
    rules[x] = list(y)
string = list(input())
q = deque(string)
for _ in range(m):
    for _ in range(len(q)):
        a = q.popleft()
        if rules.get(a) is None:
            q.append(a)
            continue
        for char in rules[a]:
            q.append(char)
print(''.join(q))