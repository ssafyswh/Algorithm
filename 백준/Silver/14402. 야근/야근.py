import sys

q = int(input())
result = 0
remain = {}
for _ in range(q):
    name, log = sys.stdin.readline().split()
    if log == '+':
        if remain.get(name) is None:
            remain[name] = 1
        else:
            remain[name] += 1
    else:
        if remain.get(name) is None or remain.get(name) == 0:
            result += 1
        else:
            remain[name] -= 1
for name in remain:
    result += remain[name]
print(result)